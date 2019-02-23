# Flare Audio Reference R1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -2.5; 60 -4.3; 66 -5.9; 72 -7.3; 79 -8.6; 87 -9.6; 96 -10.5; 106 -11.5; 116 -11.9; 128 -12.4; 141 -12.6; 155 -12.8; 170 -12.8; 187 -12.9; 206 -13.0; 227 -13.1; 249 -13.2; 274 -13.2; 302 -13.3; 332 -13.2; 365 -13.2; 402 -13.2; 442 -13.4; 486 -14.1; 535 -14.7; 588 -14.8; 647 -15.0; 712 -14.6; 783 -13.5; 861 -11.8; 947 -9.3; 1042 -6.1; 1146 -2.5; 1261 -0.5; 1387 -0.5; 1526 -0.6; 1678 -6.3; 1846 -11.4; 2031 -11.8; 2234 -7.7; 2457 -4.1; 2703 -1.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Flare Audio Reference R1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Flare Audio Reference R1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-8.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 50 Hz   | 0.4  | 11.8 dB  |
| Peaking | 93 Hz   | 0.61 | -10.9 dB |
| Peaking | 1376 Hz | 1.62 | 23.1 dB  |
| Peaking | 1771 Hz | 0.35 | -29.7 dB |
| Peaking | 3460 Hz | 0.49 | 24.2 dB  |
| Peaking | 709 Hz  | 3.33 | -2.4 dB  |
| Peaking | 1131 Hz | 5.01 | 3.4 dB   |
| Peaking | 2680 Hz | 4.15 | 4.3 dB   |
| Peaking | 5129 Hz | 0.55 | -3.8 dB  |
| Peaking | 5728 Hz | 1.89 | 6.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -9.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Flare%20Audio%20Reference%20R1/Flare%20Audio%20Reference%20R1.png)