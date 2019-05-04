# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.8; 28 -1.0; 31 -1.2; 34 -1.4; 37 -1.5; 41 -1.8; 45 -2.0; 49 -2.2; 54 -2.4; 60 -2.7; 66 -3.1; 72 -3.4; 79 -3.8; 87 -4.2; 96 -4.7; 106 -5.1; 116 -5.5; 128 -5.8; 141 -6.1; 155 -6.3; 170 -6.4; 187 -6.5; 206 -6.6; 227 -6.6; 249 -6.6; 274 -6.6; 302 -6.5; 332 -6.5; 365 -6.4; 402 -6.3; 442 -6.2; 486 -6.1; 535 -5.8; 588 -5.6; 647 -5.3; 712 -5.0; 783 -4.8; 861 -4.9; 947 -5.3; 1042 -6.0; 1146 -6.9; 1261 -7.7; 1387 -8.4; 1526 -8.9; 1678 -9.5; 1846 -10.0; 2031 -10.4; 2234 -10.2; 2457 -9.3; 2703 -8.5; 2973 -7.9; 3270 -8.0; 3597 -8.5; 3957 -9.2; 4353 -9.7; 4788 -9.4; 5267 -7.2; 5793 -4.1; 6373 -2.0; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -7.8; 15026 -12.5; 16529 -7.4; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.59 | 5.7 dB  |
| Peaking | 60 Hz    | 1.12 | 2.0 dB  |
| Peaking | 2698 Hz  | 0.78 | -3.0 dB |
| Peaking | 6398 Hz  | 5.04 | 6.0 dB  |
| Peaking | 15059 Hz | 4.08 | -6.6 dB |
| Peaking | 831 Hz   | 1.52 | 2.6 dB  |
| Peaking | 2073 Hz  | 1    | -2.5 dB |
| Peaking | 2898 Hz  | 2.25 | 3.0 dB  |
| Peaking | 4503 Hz  | 4.2  | -2.4 dB |
| Peaking | 6324 Hz  | 0.32 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20ER4XR/Etymotic%20ER4XR.png)