# Woodees iESW100B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.8; 25 -10.8; 28 -10.8; 31 -10.8; 34 -10.7; 37 -10.7; 41 -10.7; 45 -10.7; 49 -10.7; 54 -10.7; 60 -10.7; 66 -10.8; 72 -10.9; 79 -10.9; 87 -10.9; 96 -10.7; 106 -10.6; 116 -10.5; 128 -10.2; 141 -10.0; 155 -9.8; 170 -9.4; 187 -8.9; 206 -8.4; 227 -7.9; 249 -7.3; 274 -6.7; 302 -6.0; 332 -5.2; 365 -4.4; 402 -3.8; 442 -3.1; 486 -2.5; 535 -2.0; 588 -1.3; 647 -0.9; 712 -0.8; 783 -0.8; 861 -1.2; 947 -1.9; 1042 -2.3; 1146 -3.2; 1261 -3.9; 1387 -3.4; 1526 -4.3; 1678 -5.1; 1846 -5.8; 2031 -6.3; 2234 -7.0; 2457 -7.9; 2703 -8.7; 2973 -6.9; 3270 -3.1; 3597 -0.5; 3957 -0.7; 4353 -3.0; 4788 -5.2; 5267 -7.0; 5793 -10.6; 6373 -8.9; 7010 -5.0; 7711 -3.9; 8482 -6.7; 9330 -9.4; 10263 -4.4; 11289 -2.3; 12418 -2.3; 13660 -2.3; 15026 -2.3; 16529 -3.6; 18182 -2.3; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW100B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW100B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.15 | -9.1 dB  |
| Peaking | 1837 Hz  | 0.19 | 6.5 dB   |
| Peaking | 2187 Hz  | 0.86 | -11.2 dB |
| Peaking | 5912 Hz  | 3.49 | -11.1 dB |
| Peaking | 9285 Hz  | 3.8  | -8.8 dB  |
| Peaking | 1197 Hz  | 5.49 | -1.7 dB  |
| Peaking | 2216 Hz  | 1.72 | 4.5 dB   |
| Peaking | 2824 Hz  | 1.46 | -6.7 dB  |
| Peaking | 3554 Hz  | 3.43 | 6.6 dB   |
| Peaking | 16281 Hz | 3.54 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW100B/Woodees%20iESW100B.png)