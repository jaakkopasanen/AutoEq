# NuForce Primo 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.3; 31 -1.5; 34 -1.6; 37 -1.8; 41 -2.0; 45 -2.1; 49 -2.3; 54 -2.7; 60 -3.0; 66 -3.3; 72 -3.6; 79 -4.0; 87 -4.4; 96 -4.9; 106 -5.2; 116 -5.4; 128 -5.8; 141 -6.1; 155 -6.3; 170 -6.5; 187 -6.7; 206 -6.8; 227 -6.8; 249 -6.9; 274 -6.7; 302 -6.7; 332 -6.6; 365 -6.5; 402 -6.4; 442 -6.2; 486 -6.1; 535 -6.0; 588 -5.6; 647 -5.5; 712 -5.6; 783 -5.4; 861 -5.8; 947 -6.1; 1042 -6.6; 1146 -7.1; 1261 -7.7; 1387 -8.5; 1526 -9.5; 1678 -10.3; 1846 -10.6; 2031 -10.0; 2234 -8.2; 2457 -5.0; 2703 -1.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.9; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Primo 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.74 | 5.3 dB  |
| Peaking | 57 Hz   | 1.22 | 2.2 dB  |
| Peaking | 739 Hz  | 2.15 | 1.2 dB  |
| Peaking | 1890 Hz | 1.61 | -8.3 dB |
| Peaking | 3427 Hz | 0.84 | 8.4 dB  |
| Peaking | 222 Hz  | 1.92 | -0.6 dB |
| Peaking | 2843 Hz | 5.85 | 2.1 dB  |
| Peaking | 3603 Hz | 1.55 | -1.2 dB |
| Peaking | 5787 Hz | 2.34 | 4.1 dB  |
| Peaking | 7511 Hz | 1.23 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20Primo%208/NuForce%20Primo%208.png)