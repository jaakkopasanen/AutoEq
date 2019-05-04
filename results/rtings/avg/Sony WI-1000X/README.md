# Sony WI-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.5; 25 -5.0; 28 -5.4; 31 -5.4; 34 -5.1; 37 -4.8; 41 -4.5; 45 -4.5; 49 -4.5; 54 -4.6; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.7; 87 -6.1; 96 -6.4; 106 -6.6; 116 -6.8; 128 -6.9; 141 -6.8; 155 -6.7; 170 -6.5; 187 -6.3; 206 -6.2; 227 -6.1; 249 -6.1; 274 -6.2; 302 -6.3; 332 -6.2; 365 -5.9; 402 -5.4; 442 -4.8; 486 -4.6; 535 -4.9; 588 -5.1; 647 -4.0; 712 -3.1; 783 -2.4; 861 -2.0; 947 -1.7; 1042 -0.5; 1146 -1.0; 1261 -1.3; 1387 -1.2; 1526 -0.8; 1678 -1.3; 1846 -2.3; 2031 -3.6; 2234 -4.4; 2457 -3.8; 2703 -2.5; 2973 -2.0; 3270 -3.4; 3597 -5.0; 3957 -5.3; 4353 -4.2; 4788 -5.2; 5267 -7.1; 5793 -6.2; 6373 -3.0; 7010 -3.1; 7711 -4.0; 8482 -4.3; 9330 -5.1; 10263 -11.3; 11289 -14.1; 12418 -9.7; 13660 -4.6; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 117 Hz   | 1.15 | -1.8 dB  |
| Peaking | 360 Hz   | 0.44 | -2.0 dB  |
| Peaking | 1184 Hz  | 0.82 | 4.3 dB   |
| Peaking | 2181 Hz  | 5.65 | -1.8 dB  |
| Peaking | 11212 Hz | 3.84 | -11.1 dB |
| Peaking | 2939 Hz  | 6.7  | 1.8 dB   |
| Peaking | 3755 Hz  | 6.21 | -1.7 dB  |
| Peaking | 5503 Hz  | 4.4  | -4.7 dB  |
| Peaking | 6525 Hz  | 2.33 | 2.8 dB   |
| Peaking | 14051 Hz | 7.12 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-1000X/Sony%20WI-1000X.png)