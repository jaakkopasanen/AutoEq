# Monster Beats Mixr
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.1; 25 -3.4; 28 -5.0; 31 -6.3; 34 -7.3; 37 -8.0; 41 -8.7; 45 -9.2; 49 -9.5; 54 -9.8; 60 -10.0; 66 -10.2; 72 -10.2; 79 -10.0; 87 -9.9; 96 -9.9; 106 -9.9; 116 -9.9; 128 -9.9; 141 -9.9; 155 -9.9; 170 -9.6; 187 -9.5; 206 -9.2; 227 -8.6; 249 -7.8; 274 -6.7; 302 -5.3; 332 -3.8; 365 -2.1; 402 -1.3; 442 -1.3; 486 -1.3; 535 -1.8; 588 -3.9; 647 -5.8; 712 -7.2; 783 -8.0; 861 -8.3; 947 -8.6; 1042 -8.8; 1146 -8.9; 1261 -8.9; 1387 -8.9; 1526 -9.2; 1678 -9.4; 1846 -9.8; 2031 -10.3; 2234 -10.9; 2457 -11.5; 2703 -12.1; 2973 -12.1; 3270 -11.2; 3597 -9.8; 3957 -10.3; 4353 -11.7; 4788 -11.3; 5267 -8.5; 5793 -3.6; 6373 -1.9; 7010 -4.8; 7711 -7.0; 8482 -7.3; 9330 -7.3; 10263 -7.3; 11289 -7.3; 12418 -7.8; 13660 -7.4; 15026 -7.3; 16529 -7.3; 18182 -7.3; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Mixr GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Mixr ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-11.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-11.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 3.72 | 7.1 dB  |
| Peaking | 452 Hz  | 2.3  | 7.5 dB  |
| Peaking | 2782 Hz | 0.57 | -4.0 dB |
| Peaking | 4773 Hz | 4.33 | -3.3 dB |
| Peaking | 6188 Hz | 3.5  | 8.2 dB  |
| Peaking | 106 Hz  | 0.43 | -3.0 dB |
| Peaking | 345 Hz  | 2.94 | 2.8 dB  |
| Peaking | 878 Hz  | 4.42 | -0.7 dB |
| Peaking | 1633 Hz | 3.33 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 7.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Beats%20Mixr/Monster%20Beats%20Mixr.png)