# InEar StageDiver SD5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.3; 28 -6.4; 31 -6.5; 34 -6.6; 37 -6.7; 41 -6.9; 45 -7.0; 49 -7.1; 54 -7.3; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.3; 87 -8.7; 96 -9.0; 106 -9.4; 116 -9.6; 128 -9.7; 141 -9.9; 155 -10.0; 170 -10.0; 187 -9.9; 206 -9.7; 227 -9.5; 249 -9.3; 274 -9.0; 302 -8.5; 332 -8.1; 365 -7.7; 402 -7.2; 442 -6.8; 486 -6.3; 535 -5.8; 588 -5.4; 647 -5.0; 712 -4.5; 783 -4.1; 861 -4.0; 947 -4.1; 1042 -4.8; 1146 -5.9; 1261 -7.2; 1387 -8.2; 1526 -8.5; 1678 -8.3; 1846 -7.7; 2031 -6.8; 2234 -6.0; 2457 -5.1; 2703 -4.2; 2973 -3.6; 3270 -3.2; 3597 -2.4; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -3.7; 6373 -6.1; 7010 -9.4; 7711 -12.0; 8482 -10.5; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar StageDiver SD5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDiver SD5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 170 Hz  |  0.61 | -3.7 dB |
| Peaking | 930 Hz  |  0.94 | 4.1 dB  |
| Peaking | 1484 Hz |  1.47 | -4.8 dB |
| Peaking | 4683 Hz |  1.1  | 7.2 dB  |
| Peaking | 7622 Hz |  2.67 | -8.4 dB |
| Peaking | 21 Hz   |  0.96 | 0.5 dB  |
| Peaking | 5246 Hz | 16.4  | 0.8 dB  |
| Peaking | 8601 Hz |  7.61 | -0.8 dB |
| Peaking | 9712 Hz |  5.82 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/InEar%20StageDiver%20SD5/InEar%20StageDiver%20SD5.png)