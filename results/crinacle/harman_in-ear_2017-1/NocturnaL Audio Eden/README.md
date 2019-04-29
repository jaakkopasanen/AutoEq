# NocturnaL Audio Eden
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.3; 25 -1.8; 28 -2.3; 31 -2.7; 34 -3.0; 37 -3.2; 41 -3.5; 45 -3.8; 49 -4.1; 54 -4.4; 60 -4.7; 66 -5.1; 72 -5.4; 79 -5.8; 87 -6.3; 96 -6.7; 106 -7.1; 116 -7.5; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.6; 187 -8.8; 206 -9.0; 227 -9.0; 249 -9.0; 274 -9.0; 302 -9.0; 332 -8.8; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.2; 535 -8.1; 588 -7.9; 647 -7.7; 712 -7.4; 783 -7.1; 861 -6.8; 947 -6.7; 1042 -6.6; 1146 -6.5; 1261 -6.5; 1387 -7.1; 1526 -8.7; 1678 -11.2; 1846 -12.2; 2031 -9.6; 2234 -6.3; 2457 -4.5; 2703 -4.2; 2973 -4.1; 3270 -1.1; 3597 -0.5; 3957 -1.1; 4353 -3.9; 4788 -3.5; 5267 -4.1; 5793 -7.0; 6373 -4.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -16.8; 16529 -21.6; 18182 -16.9; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Eden GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Eden ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 11 Hz    |  0.24 | 5.9 dB   |
| Peaking | 231 Hz   |  0.53 | -2.9 dB  |
| Peaking | 1840 Hz  |  3.75 | -7.5 dB  |
| Peaking | 3569 Hz  |  1.12 | 5.3 dB   |
| Peaking | 16891 Hz |  1.62 | -16.8 dB |
| Peaking | 1165 Hz  |  3.94 | 0.6 dB   |
| Peaking | 2931 Hz  | 10.11 | -1.4 dB  |
| Peaking | 12201 Hz |  2    | 2.0 dB   |
| Peaking | 13557 Hz |  4.87 | 3.2 dB   |
| Peaking | 15380 Hz |  4.11 | -4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB   |
| Peaking | 62 Hz    | 1.41 | 1.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -14.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/NocturnaL%20Audio%20Eden/NocturnaL%20Audio%20Eden.png)