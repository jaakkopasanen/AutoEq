# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.1; 25 -1.9; 28 -3.2; 31 -4.4; 34 -5.4; 37 -6.2; 41 -7.2; 45 -8.1; 49 -8.9; 54 -9.7; 60 -10.5; 66 -11.1; 72 -11.7; 79 -12.2; 87 -12.6; 96 -13.0; 106 -13.3; 116 -13.4; 128 -13.3; 141 -13.1; 155 -12.8; 170 -12.2; 187 -11.5; 206 -10.7; 227 -9.7; 249 -8.7; 274 -7.6; 302 -6.2; 332 -4.5; 365 -2.7; 402 -1.5; 442 -0.8; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -1.3; 1146 -2.2; 1261 -3.4; 1387 -4.7; 1526 -5.7; 1678 -6.7; 1846 -8.3; 2031 -9.8; 2234 -11.3; 2457 -12.6; 2703 -13.8; 2973 -13.4; 3270 -12.5; 3597 -11.3; 3957 -9.1; 4353 -8.1; 4788 -10.2; 5267 -10.3; 5793 -4.4; 6373 -1.0; 7010 -4.0; 7711 -8.8; 8482 -9.1; 9330 -6.5; 10263 -6.5; 11289 -8.1; 12418 -11.3; 13660 -13.5; 15026 -13.9; 16529 -12.5; 18182 -8.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.9  | 7.2 dB   |
| Peaking | 167 Hz   | 0.37 | -11.7 dB |
| Peaking | 486 Hz   | 0.43 | 12.2 dB  |
| Peaking | 2660 Hz  | 1.46 | -9.3 dB  |
| Peaking | 15032 Hz | 1.48 | -8.4 dB  |
| Peaking | 5288 Hz  | 4.32 | -6.1 dB  |
| Peaking | 6229 Hz  | 3.52 | 9.0 dB   |
| Peaking | 8041 Hz  | 5.76 | -4.2 dB  |
| Peaking | 10033 Hz | 4.66 | 1.8 dB   |
| Peaking | 17165 Hz | 4.31 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -9.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monster%20Inspiration/Monster%20Inspiration.png)