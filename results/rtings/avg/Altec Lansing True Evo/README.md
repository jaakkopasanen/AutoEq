# Altec Lansing True Evo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.9; 28 -6.2; 31 -6.6; 34 -7.0; 37 -7.4; 41 -8.0; 45 -8.6; 49 -9.3; 54 -10.2; 60 -11.3; 66 -12.4; 72 -13.4; 79 -14.5; 87 -15.6; 96 -16.4; 106 -16.9; 116 -16.8; 128 -16.5; 141 -15.7; 155 -15.0; 170 -14.2; 187 -13.4; 206 -12.5; 227 -11.5; 249 -10.5; 274 -9.5; 302 -8.5; 332 -7.5; 365 -6.6; 402 -5.7; 442 -4.8; 486 -4.0; 535 -3.1; 588 -2.4; 647 -1.7; 712 -1.1; 783 -0.6; 861 -0.5; 947 -1.0; 1042 -1.8; 1146 -2.1; 1261 -2.5; 1387 -2.7; 1526 -2.8; 1678 -3.0; 1846 -3.2; 2031 -3.4; 2234 -3.4; 2457 -3.1; 2703 -3.4; 2973 -4.3; 3270 -5.3; 3597 -5.4; 3957 -5.2; 4353 -5.2; 4788 -5.6; 5267 -6.1; 5793 -7.4; 6373 -10.0; 7010 -10.5; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -6.5; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Altec Lansing True Evo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Altec Lansing True Evo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 94 Hz   | 1.24 | -5.6 dB |
| Peaking | 150 Hz  | 0.76 | -7.1 dB |
| Peaking | 766 Hz  | 0.83 | 6.0 dB  |
| Peaking | 2324 Hz | 0.93 | 2.2 dB  |
| Peaking | 6741 Hz | 4.9  | -5.2 dB |
| Peaking | 23 Hz   | 1.64 | 1.5 dB  |
| Peaking | 2685 Hz | 4.18 | 1.1 dB  |
| Peaking | 3338 Hz | 1.76 | -1.3 dB |
| Peaking | 4315 Hz | 2.63 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -10.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Altec%20Lansing%20True%20Evo/Altec%20Lansing%20True%20Evo.png)