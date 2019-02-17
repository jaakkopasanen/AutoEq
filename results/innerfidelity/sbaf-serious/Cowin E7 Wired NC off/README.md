# Cowin E7 Wired NC off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.7; 31 -3.1; 34 -4.4; 37 -5.5; 41 -6.7; 45 -7.8; 49 -8.6; 54 -9.2; 60 -9.3; 66 -9.5; 72 -10.4; 79 -11.8; 87 -13.4; 96 -14.8; 106 -16.0; 116 -16.4; 128 -17.3; 141 -18.4; 155 -18.6; 170 -18.4; 187 -19.3; 206 -18.9; 227 -18.1; 249 -17.2; 274 -15.8; 302 -14.4; 332 -13.2; 365 -12.2; 402 -11.5; 442 -10.0; 486 -9.2; 535 -8.3; 588 -7.3; 647 -6.9; 712 -6.9; 783 -6.5; 861 -6.7; 947 -6.5; 1042 -6.6; 1146 -7.1; 1261 -6.7; 1387 -6.3; 1526 -5.6; 1678 -5.6; 1846 -4.7; 2031 -4.0; 2234 -2.9; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -6.7; 4788 -10.6; 5267 -10.7; 5793 -10.3; 6373 -11.3; 7010 -11.5; 7711 -9.2; 8482 -8.1; 9330 -8.4; 10263 -8.5; 11289 -8.1; 12418 -7.8; 13660 -8.5; 15026 -7.6; 16529 -7.2; 18182 -10.3; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Wired NC off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Wired NC off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.52 | 6.9 dB   |
| Peaking | 129 Hz   | 0.81 | -7.9 dB  |
| Peaking | 224 Hz   | 1.03 | -7.9 dB  |
| Peaking | 3587 Hz  | 1.07 | 16.4 dB  |
| Peaking | 4899 Hz  | 0.86 | -13.7 dB |
| Peaking | 698 Hz   | 1.46 | 2.2 dB   |
| Peaking | 914 Hz   | 0.57 | -1.4 dB  |
| Peaking | 2515 Hz  | 4.81 | 1.9 dB   |
| Peaking | 8452 Hz  | 7.06 | 1.5 dB   |
| Peaking | 19409 Hz | 1.07 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -10.0 dB |
| Peaking | 250 Hz   | 1.41 | -10.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cowin%20E7%20Wired%20NC%20off/Cowin%20E7%20Wired%20NC%20off.png)