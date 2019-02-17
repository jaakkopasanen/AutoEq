# Bose QuietComfort 20 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.9; 41 -3.0; 45 -4.1; 49 -5.0; 54 -6.0; 60 -7.1; 66 -8.0; 72 -8.8; 79 -9.5; 87 -10.1; 96 -10.6; 106 -10.8; 116 -10.7; 128 -10.6; 141 -10.2; 155 -9.7; 170 -9.2; 187 -8.8; 206 -8.8; 227 -9.2; 249 -9.8; 274 -10.2; 302 -10.2; 332 -9.7; 365 -8.7; 402 -7.6; 442 -6.3; 486 -5.4; 535 -4.4; 588 -3.6; 647 -3.6; 712 -4.0; 783 -4.3; 861 -5.1; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.6; 1387 -9.8; 1526 -10.6; 1678 -9.7; 1846 -6.7; 2031 -3.2; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -5.5; 4353 -6.0; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.4; 7711 -7.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.62 | 9.9 dB   |
| Peaking | 81 Hz    | 0.35 | -6.4 dB  |
| Peaking | 1532 Hz  | 1.76 | -15.2 dB |
| Peaking | 1852 Hz  | 0.63 | 11.1 dB  |
| Peaking | 5786 Hz  | 4.86 | 4.6 dB   |
| Peaking | 332 Hz   | 1.64 | -4.8 dB  |
| Peaking | 785 Hz   | 0.43 | 6.5 dB   |
| Peaking | 1047 Hz  | 0.87 | -6.9 dB  |
| Peaking | 4167 Hz  | 9.86 | -5.5 dB  |
| Peaking | 20720 Hz | 1.76 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Passive/Bose%20QuietComfort%2020%20Passive.png)