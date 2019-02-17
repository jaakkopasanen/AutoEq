# Monster Inspiration
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.7; 25 -5.7; 28 -7.1; 31 -8.3; 34 -9.2; 37 -10.0; 41 -11.0; 45 -11.9; 49 -12.7; 54 -13.6; 60 -14.4; 66 -15.1; 72 -15.6; 79 -16.1; 87 -16.5; 96 -16.9; 106 -17.2; 116 -17.3; 128 -17.2; 141 -17.0; 155 -16.6; 170 -16.1; 187 -15.3; 206 -14.5; 227 -13.5; 249 -12.5; 274 -11.3; 302 -10.0; 332 -8.2; 365 -6.4; 402 -5.2; 442 -4.5; 486 -2.5; 535 -0.8; 588 -0.5; 647 -0.8; 712 -1.6; 783 -2.4; 861 -3.1; 947 -3.9; 1042 -4.8; 1146 -5.7; 1261 -6.9; 1387 -8.1; 1526 -9.1; 1678 -10.2; 1846 -11.6; 2031 -13.0; 2234 -14.1; 2457 -15.3; 2703 -17.0; 2973 -16.9; 3270 -16.5; 3597 -15.2; 3957 -13.2; 4353 -12.1; 4788 -13.6; 5267 -13.4; 5793 -8.7; 6373 -2.0; 7010 -6.2; 7711 -11.5; 8482 -13.1; 9330 -10.8; 10263 -9.2; 11289 -10.8; 12418 -14.8; 13660 -17.8; 15026 -18.0; 16529 -16.4; 18182 -12.3; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Inspiration GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Inspiration ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 80 Hz    | 0.75 | -11.1 dB |
| Peaking | 171 Hz   | 1.37 | -8.1 dB  |
| Peaking | 2955 Hz  | 1.21 | -13.0 dB |
| Peaking | 14642 Hz | 1.06 | -6.7 dB  |
| Peaking | 15867 Hz | 0.55 | -7.6 dB  |
| Peaking | 19 Hz    | 3.32 | 2.2 dB   |
| Peaking | 617 Hz   | 2.09 | 5.9 dB   |
| Peaking | 5404 Hz  | 3.71 | -7.4 dB  |
| Peaking | 6269 Hz  | 4.04 | 10.3 dB  |
| Peaking | 8139 Hz  | 5.29 | -5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -8.7 dB  |
| Peaking | 125 Hz   | 1.41 | -11.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB  |
| Peaking | 500 Hz   | 1.41 | 5.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -8.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -18.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monster%20Inspiration/Monster%20Inspiration.png)