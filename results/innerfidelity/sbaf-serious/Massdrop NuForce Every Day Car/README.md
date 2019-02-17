# Massdrop NuForce Every Day Car
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.3; 23 -19.3; 25 -19.2; 28 -19.0; 31 -18.8; 34 -18.6; 37 -18.4; 41 -18.2; 45 -18.0; 49 -17.8; 54 -17.5; 60 -17.2; 66 -17.0; 72 -16.8; 79 -16.5; 87 -16.4; 96 -16.2; 106 -15.9; 116 -15.4; 128 -15.2; 141 -15.0; 155 -14.7; 170 -14.3; 187 -13.8; 206 -13.3; 227 -12.7; 249 -12.3; 274 -11.7; 302 -11.1; 332 -10.5; 365 -10.0; 402 -9.2; 442 -8.5; 486 -8.1; 535 -7.7; 588 -6.9; 647 -6.6; 712 -6.5; 783 -6.2; 861 -6.3; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.7; 1387 -8.3; 1526 -9.0; 1678 -9.6; 1846 -9.7; 2031 -9.5; 2234 -9.4; 2457 -8.7; 2703 -7.7; 2973 -5.5; 3270 -2.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop NuForce Every Day Car GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop NuForce Every Day Car ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.18 | -12.5 dB |
| Peaking | 182 Hz  | 0.8  | -3.4 dB  |
| Peaking | 2163 Hz | 1.52 | -5.3 dB  |
| Peaking | 4323 Hz | 1.18 | 7.8 dB   |
| Peaking | 785 Hz  | 0.98 | 3.8 dB   |
| Peaking | 803 Hz  | 0.54 | -2.6 dB  |
| Peaking | 2087 Hz | 5.59 | 1.2 dB   |
| Peaking | 6235 Hz | 3.55 | 4.0 dB   |
| Peaking | 7737 Hz | 1.46 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20NuForce%20Every%20Day%20Car/Massdrop%20NuForce%20Every%20Day%20Car.png)