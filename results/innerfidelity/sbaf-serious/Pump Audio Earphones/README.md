# Pump Audio Earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.9; 23 -16.9; 25 -16.9; 28 -16.8; 31 -16.7; 34 -16.7; 37 -16.6; 41 -16.5; 45 -16.4; 49 -16.3; 54 -16.3; 60 -16.2; 66 -16.1; 72 -16.0; 79 -16.0; 87 -15.9; 96 -15.8; 106 -15.6; 116 -15.2; 128 -15.0; 141 -14.7; 155 -14.3; 170 -13.8; 187 -13.3; 206 -12.8; 227 -12.0; 249 -11.4; 274 -10.8; 302 -10.0; 332 -9.4; 365 -8.6; 402 -7.9; 442 -7.0; 486 -6.5; 535 -5.7; 588 -4.4; 647 -3.8; 712 -3.4; 783 -2.8; 861 -2.7; 947 -2.8; 1042 -2.9; 1146 -2.9; 1261 -3.0; 1387 -3.5; 1526 -4.0; 1678 -4.8; 1846 -5.7; 2031 -5.7; 2234 -6.1; 2457 -5.2; 2703 -4.5; 2973 -2.6; 3270 -0.9; 3597 -0.5; 3957 -1.9; 4353 -5.6; 4788 -10.1; 5267 -11.9; 5793 -4.2; 6373 -0.7; 7010 -3.6; 7711 -5.9; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pump Audio Earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pump Audio Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.19 | -10.5 dB |
| Peaking | 181 Hz   | 0.73 | -4.0 dB  |
| Peaking | 4380 Hz  | 0.37 | 34.6 dB  |
| Peaking | 5010 Hz  | 0.62 | -40.7 dB |
| Peaking | 6245 Hz  | 4.12 | 9.2 dB   |
| Peaking | 418 Hz   | 1    | -2.6 dB  |
| Peaking | 755 Hz   | 0.5  | 3.0 dB   |
| Peaking | 2146 Hz  | 1.28 | -4.0 dB  |
| Peaking | 3379 Hz  | 4.29 | 3.0 dB   |
| Peaking | 10396 Hz | 2.23 | 0.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB  |
| Peaking | 125 Hz   | 1.41 | -7.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pump%20Audio%20Earphones/Pump%20Audio%20Earphones.png)