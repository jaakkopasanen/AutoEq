# InEar PhoPhile-8 Bass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.7; 25 -3.0; 28 -3.3; 31 -3.6; 34 -3.8; 37 -3.9; 41 -4.1; 45 -4.3; 49 -4.4; 54 -4.7; 60 -4.9; 66 -5.1; 72 -5.4; 79 -5.7; 87 -5.9; 96 -6.3; 106 -6.5; 116 -6.6; 128 -6.7; 141 -6.7; 155 -6.7; 170 -6.5; 187 -6.3; 206 -6.0; 227 -5.7; 249 -5.3; 274 -5.0; 302 -4.7; 332 -4.4; 365 -4.1; 402 -4.0; 442 -3.8; 486 -3.7; 535 -3.6; 588 -3.5; 647 -3.3; 712 -3.1; 783 -2.8; 861 -2.6; 947 -2.7; 1042 -3.1; 1146 -3.8; 1261 -4.7; 1387 -5.0; 1526 -4.9; 1678 -4.4; 1846 -3.7; 2031 -3.0; 2234 -2.3; 2457 -1.5; 2703 -1.0; 2973 -1.2; 3270 -1.7; 3597 -1.5; 3957 -1.0; 4353 -0.5; 4788 -0.9; 5267 -2.9; 5793 -4.4; 6373 -3.4; 7010 -4.9; 7711 -6.9; 8482 -5.0; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -5.2; 18182 -11.2; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 Bass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 Bass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.56 | 1.6 dB   |
| Peaking | 130 Hz   | 0.88 | -3.1 dB  |
| Peaking | 2742 Hz  | 2.84 | 2.8 dB   |
| Peaking | 4333 Hz  | 3.15 | 3.4 dB   |
| Peaking | 7725 Hz  | 5.63 | -3.5 dB  |
| Peaking | 990 Hz   | 1.17 | 2.1 dB   |
| Peaking | 1367 Hz  | 1.85 | -2.7 dB  |
| Peaking | 2149 Hz  | 3.85 | 0.6 dB   |
| Peaking | 19432 Hz | 1.22 | -11.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/InEar%20PhoPhile-8%20Bass%20Treble/InEar%20PhoPhile-8%20Bass%20Treble.png)