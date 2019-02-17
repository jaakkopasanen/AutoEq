# Flare Audio Reference R1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.5; 60 -3.3; 66 -4.9; 72 -6.2; 79 -7.5; 87 -8.6; 96 -9.4; 106 -10.4; 116 -10.9; 128 -11.3; 141 -11.6; 155 -11.8; 170 -11.8; 187 -11.9; 206 -12.0; 227 -12.0; 249 -12.1; 274 -12.2; 302 -12.2; 332 -12.1; 365 -12.1; 402 -12.2; 442 -12.4; 486 -13.1; 535 -13.7; 588 -13.8; 647 -13.9; 712 -13.6; 783 -12.5; 861 -10.7; 947 -8.2; 1042 -5.0; 1146 -1.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -5.2; 1846 -10.4; 2031 -10.7; 2234 -6.7; 2457 -3.0; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Flare Audio Reference R1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Flare Audio Reference R1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 45 Hz   | 0.45 | 9.9 dB   |
| Peaking | 104 Hz  | 0.59 | -8.6 dB  |
| Peaking | 1264 Hz | 1.89 | 17.5 dB  |
| Peaking | 1336 Hz | 0.32 | -13.1 dB |
| Peaking | 3636 Hz | 0.78 | 14.0 dB  |
| Peaking | 1564 Hz | 7.33 | 5.6 dB   |
| Peaking | 1938 Hz | 4.28 | -5.7 dB  |
| Peaking | 2631 Hz | 3.54 | 4.4 dB   |
| Peaking | 5910 Hz | 2.08 | 7.3 dB   |
| Peaking | 6009 Hz | 0.83 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -8.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Flare%20Audio%20Reference%20R1/Flare%20Audio%20Reference%20R1.png)