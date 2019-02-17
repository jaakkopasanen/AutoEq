# Sony WI-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.0; 28 -2.3; 31 -2.2; 34 -1.8; 37 -1.6; 41 -1.3; 45 -1.3; 49 -1.3; 54 -1.5; 60 -2.1; 66 -2.6; 72 -3.1; 79 -3.6; 87 -4.2; 96 -4.9; 106 -5.6; 116 -6.2; 128 -6.8; 141 -7.2; 155 -7.5; 170 -7.6; 187 -7.7; 206 -7.8; 227 -7.8; 249 -7.8; 274 -7.9; 302 -8.0; 332 -7.9; 365 -7.7; 402 -7.1; 442 -6.5; 486 -6.3; 535 -6.5; 588 -6.8; 647 -5.8; 712 -4.7; 783 -4.0; 861 -3.6; 947 -3.4; 1042 -2.0; 1146 -2.6; 1261 -2.9; 1387 -2.8; 1526 -2.3; 1678 -2.8; 1846 -3.6; 2031 -4.8; 2234 -5.2; 2457 -4.6; 2703 -3.6; 2973 -3.7; 3270 -5.3; 3597 -6.9; 3957 -7.4; 4353 -6.2; 4788 -6.5; 5267 -8.4; 5793 -8.0; 6373 -5.7; 7010 -4.6; 7711 -4.4; 8482 -4.8; 9330 -8.5; 10263 -13.6; 11289 -14.8; 12418 -11.4; 13660 -6.9; 15026 -4.2; 16529 -2.9; 18182 -3.0; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 148 Hz   | 1.39 | -3.3 dB  |
| Peaking | 333 Hz   | 0.76 | -5.1 dB  |
| Peaking | 3807 Hz  | 2.36 | -4.0 dB  |
| Peaking | 5484 Hz  | 4.73 | -4.8 dB  |
| Peaking | 11183 Hz | 2.25 | -13.3 dB |
| Peaking | 18 Hz    | 2.36 | 2.8 dB   |
| Peaking | 46 Hz    | 2.4  | 1.7 dB   |
| Peaking | 1850 Hz  | 1.1  | 1.6 dB   |
| Peaking | 2143 Hz  | 3.21 | -3.6 dB  |
| Peaking | 8167 Hz  | 7.45 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-1000X/Sony%20WI-1000X.png)