# Velodyne vPulse
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.1; 23 -17.7; 25 -17.3; 28 -16.8; 31 -16.3; 34 -15.8; 37 -15.4; 41 -14.9; 45 -14.4; 49 -14.0; 54 -13.5; 60 -13.1; 66 -12.8; 72 -12.5; 79 -12.2; 87 -11.9; 96 -11.7; 106 -11.3; 116 -11.0; 128 -10.7; 141 -10.4; 155 -10.0; 170 -9.6; 187 -9.2; 206 -8.9; 227 -8.4; 249 -8.0; 274 -7.5; 302 -7.1; 332 -6.7; 365 -6.3; 402 -5.9; 442 -5.5; 486 -5.3; 535 -5.0; 588 -4.3; 647 -4.2; 712 -4.5; 783 -4.3; 861 -4.6; 947 -4.9; 1042 -5.3; 1146 -5.6; 1261 -6.1; 1387 -6.8; 1526 -7.5; 1678 -8.1; 1846 -8.3; 2031 -8.3; 2234 -8.4; 2457 -8.1; 2703 -8.3; 2973 -8.1; 3270 -7.7; 3597 -7.4; 3957 -7.7; 4353 -7.7; 4788 -5.9; 5267 -2.8; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Velodyne vPulse GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Velodyne vPulse ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.45 | -10.9 dB |
| Peaking | 45 Hz   | 0.22 | -5.2 dB  |
| Peaking | 759 Hz  | 0.65 | 4.5 dB   |
| Peaking | 1998 Hz | 0.36 | -3.2 dB  |
| Peaking | 5958 Hz | 3.08 | 8.0 dB   |
| Peaking | 1758 Hz | 4.67 | -0.6 dB  |
| Peaking | 3949 Hz | 1.78 | 1.0 dB   |
| Peaking | 4342 Hz | 4.84 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Velodyne%20vPulse/Velodyne%20vPulse.png)