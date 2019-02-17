# Life Acoustics PreKickstarter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.9; 28 -6.1; 31 -6.3; 34 -6.4; 37 -6.6; 41 -6.7; 45 -6.9; 49 -7.2; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.4; 79 -8.8; 87 -9.2; 96 -9.6; 106 -9.9; 116 -10.0; 128 -10.4; 141 -10.6; 155 -10.7; 170 -10.9; 187 -10.9; 206 -10.9; 227 -10.8; 249 -10.8; 274 -10.5; 302 -10.4; 332 -10.1; 365 -9.8; 402 -9.5; 442 -9.1; 486 -8.8; 535 -8.4; 588 -7.7; 647 -7.3; 712 -7.0; 783 -6.5; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.4; 1387 -6.4; 1526 -6.5; 1678 -6.4; 1846 -6.3; 2031 -6.2; 2234 -6.1; 2457 -4.9; 2703 -3.3; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -4.1; 4788 -3.9; 5267 -2.1; 5793 -1.1; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Life Acoustics PreKickstarter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Life Acoustics PreKickstarter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.56 | 1.2 dB  |
| Peaking | 151 Hz  | 0.62 | -4.0 dB |
| Peaking | 331 Hz  | 1.18 | -1.9 dB |
| Peaking | 3390 Hz | 2.46 | 6.5 dB  |
| Peaking | 5942 Hz | 3.66 | 5.3 dB  |
| Peaking | 502 Hz  | 4.22 | -0.6 dB |
| Peaking | 808 Hz  | 1.76 | 0.6 dB  |
| Peaking | 2277 Hz | 2.69 | -1.1 dB |
| Peaking | 2697 Hz | 4.13 | 1.1 dB  |
| Peaking | 8877 Hz | 3.72 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Life%20Acoustics%20PreKickstarter/Life%20Acoustics%20PreKickstarter.png)