# Life Acoustics PreKickstarter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.5; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.3; 41 -6.4; 45 -6.6; 49 -6.9; 54 -7.1; 60 -7.4; 66 -7.7; 72 -8.1; 79 -8.5; 87 -8.9; 96 -9.3; 106 -9.6; 116 -9.7; 128 -10.1; 141 -10.4; 155 -10.4; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.5; 249 -10.5; 274 -10.2; 302 -10.1; 332 -9.8; 365 -9.5; 402 -9.2; 442 -8.8; 486 -8.6; 535 -8.1; 588 -7.4; 647 -7.0; 712 -6.7; 783 -6.2; 861 -6.2; 947 -6.2; 1042 -6.2; 1146 -6.2; 1261 -6.1; 1387 -6.1; 1526 -6.2; 1678 -6.1; 1846 -6.0; 2031 -6.0; 2234 -5.8; 2457 -4.6; 2703 -3.0; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.8; 4788 -3.6; 5267 -1.8; 5793 -0.8; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Life Acoustics PreKickstarter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Life Acoustics PreKickstarter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.59 | 1.4 dB  |
| Peaking | 152 Hz  | 0.69 | -3.8 dB |
| Peaking | 324 Hz  | 1.32 | -1.9 dB |
| Peaking | 3378 Hz | 2.21 | 6.4 dB  |
| Peaking | 5938 Hz | 3.66 | 5.5 dB  |
| Peaking | 501 Hz  | 3.21 | -0.7 dB |
| Peaking | 816 Hz  | 1.3  | 0.7 dB  |
| Peaking | 2153 Hz | 6.27 | -0.8 dB |
| Peaking | 8579 Hz | 3.52 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Life%20Acoustics%20PreKickstarter/Life%20Acoustics%20PreKickstarter.png)