# Bose QuietComfort 35 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.5; 25 -3.4; 28 -4.4; 31 -5.2; 34 -5.9; 37 -6.4; 41 -7.0; 45 -7.5; 49 -7.8; 54 -8.1; 60 -8.2; 66 -8.2; 72 -8.3; 79 -8.1; 87 -8.2; 96 -8.6; 106 -9.9; 116 -10.8; 128 -12.2; 141 -13.0; 155 -12.0; 170 -9.9; 187 -11.3; 206 -10.4; 227 -8.9; 249 -7.7; 274 -6.4; 302 -5.7; 332 -5.2; 365 -5.2; 402 -5.4; 442 -5.7; 486 -6.5; 535 -7.2; 588 -7.6; 647 -8.4; 712 -9.4; 783 -9.7; 861 -9.7; 947 -8.7; 1042 -7.1; 1146 -5.5; 1261 -4.1; 1387 -3.3; 1526 -2.5; 1678 -2.5; 1846 -2.8; 2031 -2.3; 2234 -2.0; 2457 -2.5; 2703 -3.2; 2973 -4.1; 3270 -6.2; 3597 -8.7; 3957 -8.1; 4353 -6.9; 4788 -4.5; 5267 -0.5; 5793 -5.4; 6373 -2.9; 7010 -3.7; 7711 -6.0; 8482 -6.2; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 2.72 | 4.9 dB  |
| Peaking | 140 Hz  | 1.5  | -6.5 dB |
| Peaking | 822 Hz  | 2.52 | -4.7 dB |
| Peaking | 1785 Hz | 1.3  | 4.6 dB  |
| Peaking | 5276 Hz | 8.15 | 5.7 dB  |
| Peaking | 348 Hz  | 3.35 | 2.1 dB  |
| Peaking | 2714 Hz | 3.22 | 1.9 dB  |
| Peaking | 3709 Hz | 3.92 | -4.0 dB |
| Peaking | 6619 Hz | 8.75 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wired%20Passive/Bose%20QuietComfort%2035%20Wired%20Passive.png)