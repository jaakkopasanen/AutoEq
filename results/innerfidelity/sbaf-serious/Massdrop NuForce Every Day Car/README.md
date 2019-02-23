# Massdrop NuForce Every Day Car
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.9; 23 -18.8; 25 -18.8; 28 -18.6; 31 -18.4; 34 -18.2; 37 -18.0; 41 -17.8; 45 -17.6; 49 -17.3; 54 -17.1; 60 -16.8; 66 -16.6; 72 -16.4; 79 -16.1; 87 -16.0; 96 -15.8; 106 -15.5; 116 -15.0; 128 -14.8; 141 -14.5; 155 -14.2; 170 -13.8; 187 -13.4; 206 -12.9; 227 -12.3; 249 -11.8; 274 -11.3; 302 -10.7; 332 -10.1; 365 -9.6; 402 -8.8; 442 -8.1; 486 -7.7; 535 -7.3; 588 -6.5; 647 -6.2; 712 -6.1; 783 -5.8; 861 -5.8; 947 -5.9; 1042 -6.3; 1146 -6.7; 1261 -7.3; 1387 -7.9; 1526 -8.6; 1678 -9.2; 1846 -9.3; 2031 -9.1; 2234 -9.0; 2457 -8.3; 2703 -7.3; 2973 -5.1; 3270 -2.2; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop NuForce Every Day Car GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop NuForce Every Day Car ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.4  | -9.2 dB |
| Peaking | 78 Hz   | 0.23 | -8.4 dB |
| Peaking | 723 Hz  | 0.7  | 2.8 dB  |
| Peaking | 2114 Hz | 1.04 | -5.5 dB |
| Peaking | 4204 Hz | 1.12 | 8.4 dB  |
| Peaking | 3471 Hz | 5.74 | 2.6 dB  |
| Peaking | 4130 Hz | 1.62 | -1.7 dB |
| Peaking | 6358 Hz | 2.45 | 4.0 dB  |
| Peaking | 7462 Hz | 3.28 | -2.6 dB |
| Peaking | 8917 Hz | 1.14 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20NuForce%20Every%20Day%20Car/Massdrop%20NuForce%20Every%20Day%20Car.png)