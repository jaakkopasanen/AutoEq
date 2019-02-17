# Obravo HAMT1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.0; 28 -1.8; 31 -2.8; 34 -3.6; 37 -4.1; 41 -4.4; 45 -4.8; 49 -5.6; 54 -7.7; 60 -10.9; 66 -12.7; 72 -14.2; 79 -15.7; 87 -17.0; 96 -17.8; 106 -18.1; 116 -17.6; 128 -16.7; 141 -15.4; 155 -13.9; 170 -12.2; 187 -10.9; 206 -8.9; 227 -6.5; 249 -3.9; 274 -0.7; 302 -0.5; 332 -0.5; 365 -1.0; 402 -5.9; 442 -9.8; 486 -14.1; 535 -16.8; 588 -15.6; 647 -13.5; 712 -11.7; 783 -9.9; 861 -8.6; 947 -7.3; 1042 -5.9; 1146 -4.2; 1261 -2.6; 1387 -1.3; 1526 -0.5; 1678 -0.5; 1846 -2.6; 2031 -9.3; 2234 -10.1; 2457 -8.2; 2703 -7.9; 2973 -8.7; 3270 -9.6; 3597 -9.9; 3957 -9.4; 4353 -7.9; 4788 -4.9; 5267 -2.9; 5793 -2.6; 6373 -2.1; 7010 -4.0; 7711 -6.4; 8482 -11.9; 9330 -14.7; 10263 -12.9; 11289 -8.3; 12418 -6.5; 13660 -7.2; 15026 -9.5; 16529 -10.2; 18182 -11.0; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Obravo HAMT1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Obravo HAMT1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 1.16 | -12.8 dB |
| Peaking | 324 Hz   | 1.78 | 11.6 dB  |
| Peaking | 541 Hz   | 1.91 | -12.8 dB |
| Peaking | 1459 Hz  | 3.17 | 7.6 dB   |
| Peaking | 19765 Hz | 0.14 | -4.4 dB  |
| Peaking | 24 Hz    | 1.29 | 6.8 dB   |
| Peaking | 2175 Hz  | 7.05 | -6.0 dB  |
| Peaking | 3728 Hz  | 1.3  | -11.1 dB |
| Peaking | 6096 Hz  | 0.53 | 11.8 dB  |
| Peaking | 9217 Hz  | 2.29 | -14.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | -4.7 dB  |
| Peaking | 125 Hz   | 1.41 | -14.2 dB |
| Peaking | 250 Hz   | 1.41 | 9.8 dB   |
| Peaking | 500 Hz   | 1.41 | -8.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -4.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Obravo%20HAMT1/Obravo%20HAMT1.png)