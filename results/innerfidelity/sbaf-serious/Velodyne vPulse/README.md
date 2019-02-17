# Velodyne vPulse
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.0; 23 -18.6; 25 -18.2; 28 -17.7; 31 -17.1; 34 -16.6; 37 -16.2; 41 -15.7; 45 -15.2; 49 -14.8; 54 -14.4; 60 -13.9; 66 -13.6; 72 -13.3; 79 -13.1; 87 -12.8; 96 -12.6; 106 -12.2; 116 -11.8; 128 -11.6; 141 -11.2; 155 -10.9; 170 -10.5; 187 -10.1; 206 -9.7; 227 -9.3; 249 -8.9; 274 -8.4; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.8; 442 -6.3; 486 -6.1; 535 -5.8; 588 -5.2; 647 -5.0; 712 -5.3; 783 -5.1; 861 -5.5; 947 -5.7; 1042 -6.1; 1146 -6.5; 1261 -6.9; 1387 -7.6; 1526 -8.4; 1678 -8.9; 1846 -9.1; 2031 -9.2; 2234 -9.3; 2457 -9.0; 2703 -9.1; 2973 -8.9; 3270 -8.6; 3597 -8.3; 3957 -8.5; 4353 -8.6; 4788 -6.8; 5267 -3.7; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.2; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Velodyne vPulse GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Velodyne vPulse ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.23 | -13.1 dB |
| Peaking | 144 Hz   | 0.88 | -2.8 dB  |
| Peaking | 1984 Hz  | 1.95 | -2.8 dB  |
| Peaking | 4568 Hz  | 0.95 | -4.2 dB  |
| Peaking | 5982 Hz  | 2.73 | 9.4 dB   |
| Peaking | 278 Hz   | 1.89 | -0.6 dB  |
| Peaking | 689 Hz   | 1.35 | 1.5 dB   |
| Peaking | 1424 Hz  | 3.95 | -0.4 dB  |
| Peaking | 1559 Hz  | 4.62 | -0.5 dB  |
| Peaking | 11840 Hz | 3.28 | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Velodyne%20vPulse/Velodyne%20vPulse.png)