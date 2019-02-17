# NuForce NE700M 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.4; 25 -15.2; 28 -14.9; 31 -14.6; 34 -14.3; 37 -14.0; 41 -13.7; 45 -13.4; 49 -13.1; 54 -12.8; 60 -12.4; 66 -12.3; 72 -12.0; 79 -11.8; 87 -11.7; 96 -11.5; 106 -11.1; 116 -10.7; 128 -10.5; 141 -10.1; 155 -9.8; 170 -9.3; 187 -8.9; 206 -8.5; 227 -7.9; 249 -7.4; 274 -6.9; 302 -6.4; 332 -5.8; 365 -5.3; 402 -4.9; 442 -4.3; 486 -4.0; 535 -3.6; 588 -3.0; 647 -2.8; 712 -2.7; 783 -2.4; 861 -2.7; 947 -3.0; 1042 -3.6; 1146 -4.1; 1261 -4.7; 1387 -5.6; 1526 -6.7; 1678 -7.5; 1846 -8.0; 2031 -8.5; 2234 -9.4; 2457 -10.1; 2703 -10.5; 2973 -8.7; 3270 -5.6; 3597 -4.0; 3957 -4.5; 4353 -6.9; 4788 -8.0; 5267 -6.6; 5793 -3.4; 6373 -0.5; 7010 -0.9; 7711 -3.1; 8482 -3.4; 9330 -3.4; 10263 -3.6; 11289 -3.5; 12418 -3.4; 13660 -3.7; 15026 -8.1; 16529 -5.6; 18182 -3.4; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce NE700M 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce NE700M 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.19 | -11.9 dB |
| Peaking | 153 Hz   | 0.84 | -3.2 dB  |
| Peaking | 1737 Hz  | 3.18 | -2.8 dB  |
| Peaking | 2555 Hz  | 2.22 | -6.9 dB  |
| Peaking | 15537 Hz | 3.62 | -5.4 dB  |
| Peaking | 280 Hz   | 2.14 | -0.7 dB  |
| Peaking | 727 Hz   | 1.82 | 1.7 dB   |
| Peaking | 3708 Hz  | 4.17 | 3.5 dB   |
| Peaking | 4844 Hz  | 2.17 | -5.1 dB  |
| Peaking | 6503 Hz  | 3.69 | 5.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -3.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20NE700M%202013/NuForce%20NE700M%202013.png)