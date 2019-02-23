# Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.9; 60 -1.5; 66 -1.9; 72 -2.4; 79 -2.9; 87 -3.5; 96 -4.0; 106 -4.5; 116 -5.0; 128 -5.5; 141 -6.0; 155 -6.3; 170 -6.6; 187 -6.9; 206 -7.1; 227 -7.3; 249 -7.4; 274 -7.3; 302 -7.2; 332 -7.1; 365 -7.0; 402 -7.0; 442 -7.0; 486 -7.0; 535 -6.9; 588 -6.9; 647 -6.9; 712 -7.0; 783 -7.1; 861 -7.1; 947 -6.9; 1042 -6.7; 1146 -6.5; 1261 -5.8; 1387 -4.9; 1526 -3.9; 1678 -3.1; 1846 -2.7; 2031 -2.8; 2234 -3.4; 2457 -4.8; 2703 -6.8; 2973 -7.4; 3270 -6.5; 3597 -5.2; 3957 -5.4; 4353 -7.8; 4788 -9.8; 5267 -8.2; 5793 -8.1; 6373 -10.1; 7010 -9.6; 7711 -9.5; 8482 -8.6; 9330 -6.5; 10263 -8.0; 11289 -13.6; 12418 -14.0; 13660 -11.4; 15026 -13.0; 16529 -17.1; 18182 -18.5; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S (Dekoni Fenestrated Sheepskin earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.63 | 6.8 dB  |
| Peaking | 1889 Hz  | 2.57 | 4.4 dB  |
| Peaking | 6495 Hz  | 3.31 | -2.6 dB |
| Peaking | 17617 Hz | 0.43 | -5.4 dB |
| Peaking | 19606 Hz | 0.4  | -7.7 dB |
| Peaking | 296 Hz   | 0.71 | -1.1 dB |
| Peaking | 3798 Hz  | 7.91 | 2.2 dB  |
| Peaking | 4736 Hz  | 7.62 | -2.8 dB |
| Peaking | 9721 Hz  | 4.91 | 3.8 dB  |
| Peaking | 11696 Hz | 5.33 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | 0.3 dB   |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -13.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800%20S%20(Dekoni%20Fenestrated%20Sheepskin%20earpads)/Sennheiser%20HD%20800%20S%20(Dekoni%20Fenestrated%20Sheepskin%20earpads).png)