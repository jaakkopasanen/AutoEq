# Earsonics Velvet Pot CCW
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.6; 28 -6.8; 31 -6.9; 34 -7.0; 37 -7.0; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.0; 66 -6.9; 72 -6.8; 79 -6.7; 87 -6.4; 96 -6.1; 106 -5.4; 116 -4.8; 128 -4.0; 141 -3.1; 155 -2.0; 170 -1.0; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -1.0; 302 -1.9; 332 -2.6; 365 -3.3; 402 -3.9; 442 -4.3; 486 -4.8; 535 -5.1; 588 -5.0; 647 -5.1; 712 -5.4; 783 -5.4; 861 -5.8; 947 -6.2; 1042 -6.6; 1146 -7.0; 1261 -7.4; 1387 -7.9; 1526 -8.2; 1678 -8.0; 1846 -7.0; 2031 -4.9; 2234 -3.2; 2457 -1.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot CCW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CCW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.63 | -1.8 dB |
| Peaking | 207 Hz  | 0.86 | 7.0 dB  |
| Peaking | 1578 Hz | 1.83 | -4.5 dB |
| Peaking | 3515 Hz | 0.77 | 7.1 dB  |
| Peaking | 2643 Hz | 4.77 | 1.2 dB  |
| Peaking | 3512 Hz | 2.43 | -0.9 dB |
| Peaking | 6137 Hz | 2.52 | 5.3 dB  |
| Peaking | 7262 Hz | 1.39 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 6.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CCW/Earsonics%20Velvet%20Pot%20CCW.png)