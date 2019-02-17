# First Harmonic IEB6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.7; 31 -3.4; 34 -4.0; 37 -4.6; 41 -5.3; 45 -5.9; 49 -6.4; 54 -7.1; 60 -7.8; 66 -8.4; 72 -9.0; 79 -9.5; 87 -10.1; 96 -10.6; 106 -11.0; 116 -11.2; 128 -11.4; 141 -11.7; 155 -11.7; 170 -11.7; 187 -11.5; 206 -11.4; 227 -11.0; 249 -10.8; 274 -10.4; 302 -9.9; 332 -9.4; 365 -8.8; 402 -8.4; 442 -7.7; 486 -7.3; 535 -6.8; 588 -6.0; 647 -5.6; 712 -5.4; 783 -4.9; 861 -5.1; 947 -5.4; 1042 -5.8; 1146 -6.3; 1261 -6.8; 1387 -7.6; 1526 -8.2; 1678 -8.7; 1846 -9.0; 2031 -9.2; 2234 -9.8; 2457 -7.7; 2703 -9.4; 2973 -10.9; 3270 -10.2; 3597 -8.7; 3957 -8.4; 4353 -10.1; 4788 -11.3; 5267 -12.7; 5793 -16.6; 6373 -15.6; 7010 -10.6; 7711 -7.2; 8482 -5.7; 9330 -5.7; 10263 -7.2; 11289 -8.6; 12418 -6.8; 13660 -6.7; 15026 -8.6; 16529 -6.0; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`First Harmonic IEB6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `First Harmonic IEB6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.01 | 5.6 dB   |
| Peaking | 149 Hz   | 0.57 | -6.5 dB  |
| Peaking | 1898 Hz  | 2.43 | -3.2 dB  |
| Peaking | 3069 Hz  | 2.99 | -4.0 dB  |
| Peaking | 5921 Hz  | 3.01 | -11.5 dB |
| Peaking | 312 Hz   | 2.32 | -0.7 dB  |
| Peaking | 766 Hz   | 2.2  | 1.7 dB   |
| Peaking | 4551 Hz  | 9.22 | -1.3 dB  |
| Peaking | 8570 Hz  | 2.74 | 3.1 dB   |
| Peaking | 12089 Hz | 0.75 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/First%20Harmonic%20IEB6/First%20Harmonic%20IEB6.png)