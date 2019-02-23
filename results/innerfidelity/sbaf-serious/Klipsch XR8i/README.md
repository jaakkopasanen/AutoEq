# Klipsch XR8i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.6; 25 -13.6; 28 -13.7; 31 -13.7; 34 -13.6; 37 -13.6; 41 -13.5; 45 -13.5; 49 -13.4; 54 -13.4; 60 -13.3; 66 -13.3; 72 -13.2; 79 -13.2; 87 -13.2; 96 -13.2; 106 -13.0; 116 -12.8; 128 -12.6; 141 -12.4; 155 -12.1; 170 -11.8; 187 -11.4; 206 -11.0; 227 -10.5; 249 -10.3; 274 -9.9; 302 -9.5; 332 -9.1; 365 -8.7; 402 -8.3; 442 -7.7; 486 -7.5; 535 -7.1; 588 -6.5; 647 -6.2; 712 -6.1; 783 -5.8; 861 -5.9; 947 -6.1; 1042 -6.3; 1146 -6.6; 1261 -6.8; 1387 -7.3; 1526 -7.7; 1678 -7.8; 1846 -7.7; 2031 -7.5; 2234 -7.4; 2457 -6.9; 2703 -6.3; 2973 -4.6; 3270 -2.2; 3597 -0.9; 3957 -1.2; 4353 -2.8; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch XR8i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch XR8i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.14 | -7.2 dB |
| Peaking | 663 Hz  | 1.9  | 1.6 dB  |
| Peaking | 3638 Hz | 4.35 | 5.2 dB  |
| Peaking | 5801 Hz | 2.13 | 6.9 dB  |
| Peaking | 7935 Hz | 2    | -1.8 dB |
| Peaking | 982 Hz  | 2.02 | 0.7 dB  |
| Peaking | 1874 Hz | 1.33 | -1.6 dB |
| Peaking | 3224 Hz | 7.28 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20XR8i/Klipsch%20XR8i.png)