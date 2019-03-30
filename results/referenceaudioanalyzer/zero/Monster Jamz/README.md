# Monster Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.1; 23 -16.1; 25 -16.1; 28 -16.1; 31 -16.1; 34 -16.1; 37 -16.1; 41 -16.0; 45 -15.9; 49 -15.8; 54 -15.7; 60 -15.6; 66 -15.5; 72 -15.4; 79 -15.2; 87 -15.0; 96 -14.8; 106 -14.5; 116 -14.3; 128 -14.1; 141 -14.2; 155 -14.2; 170 -14.2; 187 -14.2; 206 -14.2; 227 -13.9; 249 -13.6; 274 -13.3; 302 -13.0; 332 -12.7; 365 -12.3; 402 -11.9; 442 -11.6; 486 -11.2; 535 -10.9; 588 -10.5; 647 -10.2; 712 -9.8; 783 -9.4; 861 -9.0; 947 -8.5; 1042 -8.0; 1146 -7.3; 1261 -6.5; 1387 -5.6; 1526 -4.9; 1678 -4.0; 1846 -3.0; 2031 -2.0; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.0; 4788 -4.7; 5267 -5.3; 5793 -4.1; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.32 | -8.6 dB |
| Peaking | 209 Hz  | 0.27 | -6.4 dB |
| Peaking | 2373 Hz | 1.07 | 4.2 dB  |
| Peaking | 3393 Hz | 0.97 | 3.6 dB  |
| Peaking | 121 Hz  | 5.12 | 0.4 dB  |
| Peaking | 3825 Hz | 5.17 | 1.5 dB  |
| Peaking | 5142 Hz | 2.61 | -2.0 dB |
| Peaking | 6542 Hz | 4.54 | 5.6 dB  |
| Peaking | 7233 Hz | 1.59 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Jamz/Monster%20Jamz.png)