# VSonic VSD2S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.5; 25 -2.0; 28 -2.5; 31 -2.9; 34 -3.3; 37 -3.7; 41 -4.1; 45 -4.4; 49 -4.8; 54 -5.1; 60 -5.6; 66 -6.0; 72 -6.5; 79 -7.0; 87 -7.4; 96 -8.1; 106 -8.5; 116 -9.0; 128 -9.5; 141 -9.9; 155 -10.3; 170 -10.6; 187 -10.8; 206 -11.0; 227 -11.2; 249 -11.2; 274 -11.2; 302 -11.3; 332 -11.2; 365 -11.2; 402 -11.1; 442 -10.9; 486 -10.7; 535 -10.4; 588 -10.0; 647 -9.4; 712 -8.6; 783 -7.7; 861 -6.7; 947 -5.5; 1042 -4.7; 1146 -4.4; 1261 -4.2; 1387 -3.6; 1526 -2.5; 1678 -1.0; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.4; 3957 -1.5; 4353 -1.1; 4788 -1.5; 5267 -2.9; 5793 -5.9; 6373 -11.0; 7010 -12.1; 7711 -14.3; 8482 -12.0; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -8.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD2S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD2S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 403 Hz  | 0.29 | -6.2 dB  |
| Peaking | 2125 Hz | 0.43 | 8.1 dB   |
| Peaking | 4865 Hz | 3.58 | 2.8 dB   |
| Peaking | 7350 Hz | 2.32 | -10.5 dB |
| Peaking | 18 Hz   | 0.75 | 5.5 dB   |
| Peaking | 52 Hz   | 0.79 | 1.4 dB   |
| Peaking | 998 Hz  | 5.75 | 0.9 dB   |
| Peaking | 1342 Hz | 7.32 | -0.9 dB  |
| Peaking | 9594 Hz | 8.65 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/VSonic%20VSD2S/VSonic%20VSD2S.png)