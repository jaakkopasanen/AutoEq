# Altec Lansing True Evo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.1; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.3; 37 -2.7; 41 -3.3; 45 -3.9; 49 -4.6; 54 -5.6; 60 -6.9; 66 -8.3; 72 -9.5; 79 -10.8; 87 -12.2; 96 -13.4; 106 -14.3; 116 -14.8; 128 -14.8; 141 -14.6; 155 -14.2; 170 -13.8; 187 -13.2; 206 -12.6; 227 -11.7; 249 -10.7; 274 -9.7; 302 -8.7; 332 -7.7; 365 -6.8; 402 -5.9; 442 -4.9; 486 -4.1; 535 -3.2; 588 -2.5; 647 -1.8; 712 -1.1; 783 -0.6; 861 -0.5; 947 -1.0; 1042 -1.8; 1146 -2.0; 1261 -2.5; 1387 -2.7; 1526 -2.8; 1678 -2.9; 1846 -3.0; 2031 -3.1; 2234 -2.7; 2457 -2.3; 2703 -3.0; 2973 -4.4; 3270 -5.6; 3597 -5.9; 3957 -5.7; 4353 -5.7; 4788 -5.3; 5267 -5.8; 5793 -7.6; 6373 -11.1; 7010 -10.6; 7711 -6.9; 8482 -4.8; 9330 -5.5; 10263 -5.5; 11289 -2.7; 12418 -1.5; 13660 -2.8; 15026 -6.4; 16529 -7.1; 18182 -6.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Altec Lansing True Evo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Altec Lansing True Evo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 109 Hz   | 0.95 | -11.0 dB |
| Peaking | 212 Hz   | 0.98 | -7.2 dB  |
| Peaking | 1762 Hz  | 3.52 | -1.1 dB  |
| Peaking | 3481 Hz  | 3.02 | -3.3 dB  |
| Peaking | 6715 Hz  | 1.63 | -8.8 dB  |
| Peaking | 25 Hz    | 1.38 | 1.4 dB   |
| Peaking | 373 Hz   | 2.95 | -0.9 dB  |
| Peaking | 779 Hz   | 2.74 | 2.1 dB   |
| Peaking | 8142 Hz  | 6.84 | 2.4 dB   |
| Peaking | 18782 Hz | 0.57 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB   |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -13.2 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 16000 Hz | 1.41 | -5.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Altec%20Lansing%20True%20Evo/Altec%20Lansing%20True%20Evo.png)