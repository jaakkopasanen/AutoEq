# NarMoo R1M Gunmetal Port
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -12.7; 25 -12.5; 28 -12.1; 31 -11.8; 34 -11.6; 37 -11.4; 41 -11.1; 45 -10.9; 49 -10.8; 54 -10.6; 60 -10.6; 66 -10.5; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.7; 116 -10.7; 128 -10.7; 141 -10.7; 155 -10.6; 170 -10.4; 187 -10.3; 206 -10.0; 227 -9.7; 249 -9.4; 274 -9.0; 302 -8.5; 332 -8.1; 365 -7.5; 402 -7.0; 442 -6.4; 486 -6.0; 535 -5.4; 588 -4.5; 647 -4.0; 712 -3.7; 783 -3.2; 861 -3.2; 947 -2.8; 1042 -2.7; 1146 -2.7; 1261 -2.7; 1387 -3.1; 1526 -3.4; 1678 -3.6; 1846 -3.5; 2031 -3.2; 2234 -3.1; 2457 -2.7; 2703 -3.0; 2973 -3.3; 3270 -3.5; 3597 -3.9; 3957 -5.0; 4353 -8.0; 4788 -10.4; 5267 -9.9; 5793 -5.6; 6373 -1.7; 7010 -0.5; 7711 -2.5; 8482 -2.7; 9330 -3.2; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -2.7; 15026 -2.7; 16529 -4.3; 18182 -5.9; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo R1M Gunmetal Port GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Gunmetal Port ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.22 | -10.0 dB |
| Peaking | 181 Hz   | 0.46 | -6.8 dB  |
| Peaking | 4868 Hz  | 3.68 | -9.2 dB  |
| Peaking | 5586 Hz  | 0.05 | 0.6 dB   |
| Peaking | 17791 Hz | 1.86 | -4.2 dB  |
| Peaking | 955 Hz   | 1.65 | 0.8 dB   |
| Peaking | 1734 Hz  | 2.14 | -1.1 dB  |
| Peaking | 5478 Hz  | 8.68 | -2.0 dB  |
| Peaking | 6715 Hz  | 4.23 | 3.7 dB   |
| Peaking | 8434 Hz  | 1.26 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Gunmetal%20Port/NarMoo%20R1M%20Gunmetal%20Port.png)