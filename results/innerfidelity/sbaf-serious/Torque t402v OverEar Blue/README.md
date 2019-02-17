# Torque t402v OverEar Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.6; 25 -10.2; 28 -10.9; 31 -11.5; 34 -12.1; 37 -12.5; 41 -13.1; 45 -13.5; 49 -13.8; 54 -14.2; 60 -14.5; 66 -14.9; 72 -15.2; 79 -15.4; 87 -15.5; 96 -15.9; 106 -16.6; 116 -17.3; 128 -18.1; 141 -18.3; 155 -18.7; 170 -18.1; 187 -19.2; 206 -19.7; 227 -20.1; 249 -20.2; 274 -20.0; 302 -19.2; 332 -17.8; 365 -15.7; 402 -13.5; 442 -11.0; 486 -9.0; 535 -7.0; 588 -4.4; 647 -2.2; 712 -0.9; 783 -0.5; 861 -1.6; 947 -3.6; 1042 -6.2; 1146 -7.7; 1261 -8.6; 1387 -9.2; 1526 -9.5; 1678 -7.2; 1846 -5.3; 2031 -5.0; 2234 -5.8; 2457 -6.0; 2703 -5.6; 2973 -4.5; 3270 -2.2; 3597 -2.0; 3957 -2.5; 4353 -3.1; 4788 -2.7; 5267 -1.9; 5793 -3.5; 6373 -6.5; 7010 -8.8; 7711 -10.2; 8482 -10.3; 9330 -6.5; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Torque t402v OverEar Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 254 Hz  | 0.12 | -12.6 dB |
| Peaking | 278 Hz  | 0.56 | -16.4 dB |
| Peaking | 761 Hz  | 0.4  | 30.5 dB  |
| Peaking | 1271 Hz | 0.72 | -13.4 dB |
| Peaking | 7842 Hz | 2.44 | -8.4 dB  |
| Peaking | 329 Hz  | 6.4  | -0.3 dB  |
| Peaking | 1922 Hz | 4.43 | 3.0 dB   |
| Peaking | 2986 Hz | 1.25 | -3.3 dB  |
| Peaking | 3403 Hz | 3.37 | 4.0 dB   |
| Peaking | 5309 Hz | 6.46 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -8.4 dB  |
| Peaking | 250 Hz   | 1.41 | -16.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Blue/Torque%20t402v%20OverEar%20Blue.png)