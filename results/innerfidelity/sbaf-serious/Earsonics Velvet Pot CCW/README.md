# Earsonics Velvet Pot CCW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.0; 25 -10.2; 28 -10.4; 31 -10.6; 34 -10.6; 37 -10.7; 41 -10.7; 45 -10.8; 49 -10.8; 54 -10.7; 60 -10.7; 66 -10.6; 72 -10.5; 79 -10.3; 87 -10.1; 96 -9.7; 106 -9.1; 116 -8.4; 128 -7.6; 141 -6.7; 155 -5.7; 170 -4.7; 187 -3.7; 206 -3.3; 227 -3.4; 249 -3.9; 274 -4.6; 302 -5.6; 332 -6.3; 365 -7.0; 402 -7.6; 442 -8.0; 486 -8.5; 535 -8.8; 588 -8.6; 647 -8.8; 712 -9.1; 783 -9.1; 861 -9.4; 947 -9.8; 1042 -10.3; 1146 -10.7; 1261 -11.0; 1387 -11.5; 1526 -11.8; 1678 -11.6; 1846 -10.6; 2031 -8.6; 2234 -6.9; 2457 -5.5; 2703 -3.9; 2973 -2.5; 3270 -1.7; 3597 -1.2; 3957 -0.5; 4353 -2.2; 4788 -4.7; 5267 -2.4; 5793 -0.8; 6373 -3.6; 7010 -8.3; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot CCW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CCW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 101 Hz   | 0.16 | -5.3 dB |
| Peaking | 212 Hz   | 0.96 | 8.4 dB  |
| Peaking | 1709 Hz  | 1.01 | -7.8 dB |
| Peaking | 2426 Hz  | 1.1  | 3.9 dB  |
| Peaking | 3778 Hz  | 1.24 | 5.6 dB  |
| Peaking | 4806 Hz  | 6.61 | -3.8 dB |
| Peaking | 5820 Hz  | 3.15 | 5.0 dB  |
| Peaking | 7004 Hz  | 4.2  | -4.5 dB |
| Peaking | 14386 Hz | 4.32 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.8 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CCW/Earsonics%20Velvet%20Pot%20CCW.png)