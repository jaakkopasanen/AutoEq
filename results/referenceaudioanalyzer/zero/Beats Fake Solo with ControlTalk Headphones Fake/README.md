# Beats Fake Solo with ControlTalk Headphones Fake
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.1; 87 -2.8; 96 -4.4; 106 -5.4; 116 -6.2; 128 -6.6; 141 -6.6; 155 -6.3; 170 -6.1; 187 -5.8; 206 -5.5; 227 -5.2; 249 -5.0; 274 -4.8; 302 -4.7; 332 -4.9; 365 -5.0; 402 -4.9; 442 -4.7; 486 -4.6; 535 -4.5; 588 -4.6; 647 -4.7; 712 -4.9; 783 -5.2; 861 -5.5; 947 -5.8; 1042 -6.2; 1146 -6.6; 1261 -7.1; 1387 -7.7; 1526 -8.3; 1678 -8.6; 1846 -8.5; 2031 -8.9; 2234 -10.8; 2457 -11.8; 2703 -10.4; 2973 -7.1; 3270 -4.1; 3597 -2.6; 3957 -2.7; 4353 -3.1; 4788 -5.0; 5267 -8.0; 5793 -9.5; 6373 -10.1; 7010 -11.2; 7711 -11.7; 8482 -9.5; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Fake Solo with ControlTalk Headphones Fake GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Fake Solo with ControlTalk Headphones Fake ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.63 | 7.0 dB  |
| Peaking | 530 Hz  | 0.98 | 2.1 dB  |
| Peaking | 2570 Hz | 1.56 | -8.5 dB |
| Peaking | 3567 Hz | 1.55 | 8.6 dB  |
| Peaking | 6883 Hz | 1.97 | -6.0 dB |
| Peaking | 40 Hz   | 3.06 | -1.2 dB |
| Peaking | 74 Hz   | 2.86 | 2.5 dB  |
| Peaking | 122 Hz  | 2.32 | -2.2 dB |
| Peaking | 9684 Hz | 5.69 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20Fake%20Solo%20with%20ControlTalk%20Headphones%20Fake/Beats%20Fake%20Solo%20with%20ControlTalk%20Headphones%20Fake.png)