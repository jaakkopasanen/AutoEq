# Meze Empyrean (microfiber earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.5; 25 -6.5; 28 -6.6; 31 -6.7; 34 -6.8; 37 -6.9; 41 -6.9; 45 -6.9; 49 -6.9; 54 -7.0; 60 -7.2; 66 -7.5; 72 -7.7; 79 -8.0; 87 -8.3; 96 -8.7; 106 -9.1; 116 -9.5; 128 -9.8; 141 -10.1; 155 -10.4; 170 -10.5; 187 -10.5; 206 -10.3; 227 -10.0; 249 -9.9; 274 -10.0; 302 -9.4; 332 -8.9; 365 -8.6; 402 -8.9; 442 -8.8; 486 -7.8; 535 -6.9; 588 -7.0; 647 -7.3; 712 -7.2; 783 -7.2; 861 -7.3; 947 -6.2; 1042 -5.5; 1146 -5.0; 1261 -4.0; 1387 -3.2; 1526 -2.5; 1678 -1.4; 1846 -0.8; 2031 -0.5; 2234 -1.1; 2457 -2.0; 2703 -2.9; 2973 -3.7; 3270 -4.8; 3597 -6.0; 3957 -5.8; 4353 -5.4; 4788 -5.4; 5267 -5.5; 5793 -5.4; 6373 -4.3; 7010 -4.0; 7711 -5.9; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.4; 15026 -9.9; 16529 -13.8; 18182 -14.5; 20000 -15.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Empyrean (microfiber earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Empyrean (microfiber earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 173 Hz   | 0.64 | -3.8 dB  |
| Peaking | 767 Hz   | 0.22 | -1.1 dB  |
| Peaking | 1921 Hz  | 1.28 | 6.7 dB   |
| Peaking | 13255 Hz | 0.57 | 6.3 dB   |
| Peaking | 17805 Hz | 0.4  | -11.7 dB |
| Peaking | 1284 Hz  | 6.49 | 0.4 dB   |
| Peaking | 3637 Hz  | 8.48 | -1.2 dB  |
| Peaking | 6733 Hz  | 4.82 | 2.4 dB   |
| Peaking | 8591 Hz  | 1.61 | -0.9 dB  |
| Peaking | 13554 Hz | 5.37 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%20Empyrean%20(microfiber%20earpads)/Meze%20Empyrean%20(microfiber%20earpads).png)