# NocturnaL Audio Avalon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.7; 28 -8.1; 31 -8.4; 34 -8.6; 37 -8.8; 41 -9.0; 45 -9.2; 49 -9.5; 54 -9.7; 60 -10.0; 66 -10.3; 72 -10.6; 79 -10.9; 87 -11.3; 96 -11.7; 106 -12.1; 116 -12.4; 128 -12.7; 141 -12.9; 155 -13.0; 170 -13.1; 187 -13.2; 206 -13.2; 227 -13.1; 249 -12.9; 274 -12.7; 302 -12.4; 332 -12.0; 365 -11.5; 402 -11.1; 442 -10.7; 486 -10.1; 535 -9.5; 588 -8.9; 647 -8.2; 712 -7.4; 783 -6.6; 861 -5.8; 947 -5.3; 1042 -5.0; 1146 -5.0; 1261 -4.8; 1387 -4.2; 1526 -3.3; 1678 -2.3; 1846 -1.5; 2031 -1.0; 2234 -1.3; 2457 -1.9; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.1; 5793 -7.2; 6373 -8.3; 7010 -8.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.6; 15026 -25.8; 16529 -23.7; 18182 -12.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NocturnaL Audio Avalon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NocturnaL Audio Avalon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 100 Hz   | 0.43 | -3.5 dB  |
| Peaking | 260 Hz   | 0.57 | -4.8 dB  |
| Peaking | 2326 Hz  | 0.76 | 5.7 dB   |
| Peaking | 4271 Hz  | 2.95 | 4.2 dB   |
| Peaking | 15775 Hz | 2.18 | -22.6 dB |
| Peaking | 3236 Hz  | 6.68 | 1.0 dB   |
| Peaking | 5030 Hz  | 9.4  | 2.7 dB   |
| Peaking | 6327 Hz  | 3.89 | -3.6 dB  |
| Peaking | 11798 Hz | 3.53 | 4.7 dB   |
| Peaking | 22050 Hz | 1.88 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -18.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/NocturnaL%20Audio%20Avalon/NocturnaL%20Audio%20Avalon.png)