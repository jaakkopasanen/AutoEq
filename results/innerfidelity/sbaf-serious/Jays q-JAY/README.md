# Jays q-JAY
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.1; 25 -3.1; 28 -3.3; 31 -3.4; 34 -3.5; 37 -3.5; 41 -3.6; 45 -3.8; 49 -3.9; 54 -4.1; 60 -4.5; 66 -4.8; 72 -5.2; 79 -5.5; 87 -6.0; 96 -6.3; 106 -6.6; 116 -6.8; 128 -7.2; 141 -7.5; 155 -7.7; 170 -7.8; 187 -7.9; 206 -8.1; 227 -8.0; 249 -8.0; 274 -8.0; 302 -7.8; 332 -7.8; 365 -7.6; 402 -7.5; 442 -7.1; 486 -7.1; 535 -6.9; 588 -6.4; 647 -6.2; 712 -6.1; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.7; 1261 -6.9; 1387 -7.3; 1526 -7.6; 1678 -7.6; 1846 -7.1; 2031 -6.6; 2234 -5.9; 2457 -4.6; 2703 -3.2; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.2; 4788 -2.6; 5267 -0.8; 5793 -0.5; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -7.6; 9330 -9.6; 10263 -11.6; 11289 -10.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays q-JAY GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays q-JAY ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.37 | 3.6 dB  |
| Peaking | 48 Hz    | 2.15 | 2.2 dB  |
| Peaking | 3384 Hz  | 2.62 | 6.3 dB  |
| Peaking | 5775 Hz  | 2.53 | 6.0 dB  |
| Peaking | 10209 Hz | 2.94 | -5.9 dB |
| Peaking | 70 Hz    | 2.7  | 0.9 dB  |
| Peaking | 214 Hz   | 0.92 | -1.7 dB |
| Peaking | 1675 Hz  | 2.7  | -1.7 dB |
| Peaking | 2891 Hz  | 7.76 | 1.2 dB  |
| Peaking | 12573 Hz | 6.59 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20q-JAY/Jays%20q-JAY.png)