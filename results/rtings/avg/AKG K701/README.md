# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.8; 60 -1.1; 66 -1.5; 72 -1.8; 79 -2.2; 87 -2.6; 96 -3.1; 106 -3.5; 116 -4.0; 128 -4.4; 141 -4.7; 155 -4.9; 170 -5.1; 187 -5.2; 206 -5.2; 227 -5.2; 249 -5.2; 274 -5.3; 302 -5.4; 332 -5.4; 365 -5.3; 402 -5.4; 442 -5.4; 486 -5.2; 535 -4.6; 588 -3.8; 647 -3.7; 712 -3.3; 783 -3.2; 861 -3.5; 947 -3.9; 1042 -4.4; 1146 -4.7; 1261 -5.0; 1387 -5.5; 1526 -6.0; 1678 -7.3; 1846 -9.1; 2031 -10.1; 2234 -11.0; 2457 -10.4; 2703 -9.7; 2973 -8.7; 3270 -7.9; 3597 -7.1; 3957 -6.9; 4353 -6.8; 4788 -6.9; 5267 -7.8; 5793 -9.4; 6373 -11.5; 7010 -12.0; 7711 -12.0; 8482 -12.1; 9330 -9.1; 10263 -7.0; 11289 -9.5; 12418 -9.4; 13660 -6.5; 15026 -6.5; 16529 -7.8; 18182 -12.9; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.39 | 6.4 dB  |
| Peaking | 824 Hz   | 0.97 | 3.3 dB  |
| Peaking | 2236 Hz  | 2.33 | -5.1 dB |
| Peaking | 7517 Hz  | 1.97 | -6.1 dB |
| Peaking | 19002 Hz | 1.27 | -7.7 dB |
| Peaking | 2923 Hz  | 2.86 | -1.0 dB |
| Peaking | 4822 Hz  | 0.95 | 1.1 dB  |
| Peaking | 6266 Hz  | 5.19 | -2.0 dB |
| Peaking | 11888 Hz | 6.27 | -3.4 dB |
| Peaking | 14786 Hz | 2    | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K701/AKG%20K701.png)