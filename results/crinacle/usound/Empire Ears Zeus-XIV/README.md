# Empire Ears Zeus-XIV
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.1; 37 -1.6; 41 -2.1; 45 -2.7; 49 -3.2; 54 -3.7; 60 -4.2; 66 -4.8; 72 -5.3; 79 -5.8; 87 -6.3; 96 -6.9; 106 -7.4; 116 -7.9; 128 -8.3; 141 -8.6; 155 -8.8; 170 -9.0; 187 -9.1; 206 -9.2; 227 -9.2; 249 -9.1; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.3; 402 -8.1; 442 -7.8; 486 -7.5; 535 -7.2; 588 -6.9; 647 -6.6; 712 -6.3; 783 -6.1; 861 -6.0; 947 -6.4; 1042 -7.3; 1146 -8.9; 1261 -10.5; 1387 -11.2; 1526 -9.7; 1678 -7.1; 1846 -5.7; 2031 -6.1; 2234 -6.8; 2457 -5.8; 2703 -2.9; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.2; 5793 -5.1; 6373 -8.6; 7010 -12.6; 7711 -13.1; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Zeus-XIV GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Zeus-XIV ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.56 | 6.3 dB   |
| Peaking | 189 Hz  | 0.69 | -3.2 dB  |
| Peaking | 1375 Hz | 3.37 | -5.7 dB  |
| Peaking | 4241 Hz | 1.06 | 7.5 dB   |
| Peaking | 7253 Hz | 3.22 | -10.3 dB |
| Peaking | 818 Hz  | 3.51 | 1.1 dB   |
| Peaking | 2327 Hz | 6.06 | -2.6 dB  |
| Peaking | 2970 Hz | 6.36 | 2.1 dB   |
| Peaking | 8054 Hz | 7.99 | -1.6 dB  |
| Peaking | 8802 Hz | 5.74 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Zeus-XIV/Empire%20Ears%20Zeus-XIV.png)