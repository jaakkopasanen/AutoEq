# Sony WF-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.6; 31 -0.7; 34 -0.7; 37 -0.7; 41 -0.7; 45 -0.8; 49 -1.0; 54 -1.2; 60 -1.8; 66 -2.3; 72 -2.7; 79 -3.2; 87 -3.9; 96 -4.5; 106 -5.1; 116 -5.7; 128 -6.2; 141 -6.5; 155 -6.8; 170 -7.0; 187 -7.1; 206 -7.0; 227 -6.7; 249 -6.5; 274 -6.5; 302 -6.5; 332 -6.8; 365 -6.9; 402 -7.1; 442 -7.0; 486 -6.9; 535 -6.5; 588 -6.1; 647 -5.6; 712 -5.0; 783 -4.7; 861 -4.2; 947 -3.6; 1042 -4.2; 1146 -4.7; 1261 -5.1; 1387 -5.3; 1526 -2.8; 1678 -3.7; 1846 -5.3; 2031 -6.3; 2234 -6.3; 2457 -5.8; 2703 -4.8; 2973 -3.9; 3270 -3.6; 3597 -3.7; 3957 -3.8; 4353 -4.0; 4788 -3.6; 5267 -4.0; 5793 -4.7; 6373 -5.6; 7010 -3.8; 7711 -3.8; 8482 -4.0; 9330 -5.1; 10263 -10.8; 11289 -12.0; 12418 -7.8; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -6.0; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.33 | 4.0 dB  |
| Peaking | 152 Hz   | 0.68 | -4.2 dB |
| Peaking | 446 Hz   | 1.62 | -2.4 dB |
| Peaking | 2170 Hz  | 4.61 | -2.6 dB |
| Peaking | 11039 Hz | 3.88 | -9.3 dB |
| Peaking | 945 Hz   | 5.21 | 1.1 dB  |
| Peaking | 1459 Hz  | 2.81 | -1.9 dB |
| Peaking | 1559 Hz  | 7.52 | 3.7 dB  |
| Peaking | 9109 Hz  | 3.12 | 2.1 dB  |
| Peaking | 10013 Hz | 6.89 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WF-1000X/Sony%20WF-1000X.png)