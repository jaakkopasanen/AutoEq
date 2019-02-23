# Torque t103z Deep
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.4; 23 -16.5; 25 -16.6; 28 -16.7; 31 -16.8; 34 -16.9; 37 -16.9; 41 -17.0; 45 -17.0; 49 -17.1; 54 -17.2; 60 -17.3; 66 -17.4; 72 -17.5; 79 -17.7; 87 -17.8; 96 -17.9; 106 -17.8; 116 -17.6; 128 -17.5; 141 -17.4; 155 -17.1; 170 -16.7; 187 -16.3; 206 -15.9; 227 -15.3; 249 -14.8; 274 -14.1; 302 -13.5; 332 -12.9; 365 -12.1; 402 -11.4; 442 -10.6; 486 -10.1; 535 -9.4; 588 -8.5; 647 -8.1; 712 -6.8; 783 -6.6; 861 -6.7; 947 -6.9; 1042 -7.2; 1146 -7.4; 1261 -7.7; 1387 -8.4; 1526 -9.1; 1678 -9.8; 1846 -10.1; 2031 -10.2; 2234 -9.5; 2457 -7.0; 2703 -4.3; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t103z Deep GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Deep ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.22 | -9.8 dB |
| Peaking | 187 Hz  | 0.58 | -5.2 dB |
| Peaking | 2019 Hz | 1.8  | -7.4 dB |
| Peaking | 3718 Hz | 0.87 | 8.0 dB  |
| Peaking | 17 Hz   | 1.34 | -1.1 dB |
| Peaking | 776 Hz  | 3.93 | 1.5 dB  |
| Peaking | 4049 Hz | 5.6  | -1.0 dB |
| Peaking | 6305 Hz | 2.43 | 5.0 dB  |
| Peaking | 7430 Hz | 1.55 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.8 dB  |
| Peaking | 125 Hz   | 1.41 | -9.1 dB  |
| Peaking | 250 Hz   | 1.41 | -6.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Deep/Torque%20t103z%20Deep.png)