# Skullcandy Push
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -9.5; 23 -9.4; 25 -9.3; 28 -9.2; 31 -9.0; 34 -8.9; 37 -8.7; 41 -8.5; 45 -8.4; 49 -8.3; 54 -8.3; 60 -8.6; 66 -8.9; 72 -9.2; 79 -9.4; 87 -9.7; 96 -10.0; 106 -10.2; 116 -10.4; 128 -10.5; 141 -10.5; 155 -10.4; 170 -10.0; 187 -9.4; 206 -8.8; 227 -8.2; 249 -7.6; 274 -7.0; 302 -6.3; 332 -5.7; 365 -5.1; 402 -4.5; 442 -3.8; 486 -3.1; 535 -2.4; 588 -1.6; 647 -0.9; 712 -0.3; 783 0.2; 861 0.5; 947 0.3; 1042 -0.3; 1146 -1.1; 1261 -1.9; 1387 -2.2; 1526 -2.3; 1678 -2.5; 1846 -2.7; 2031 -3.0; 2234 -2.8; 2457 -2.2; 2703 -2.0; 2973 -1.7; 3270 -1.7; 3597 -2.1; 3957 -3.0; 4353 -4.3; 4788 -5.3; 5267 -6.8; 5793 -7.6; 6373 -7.2; 7010 -6.6; 7711 -8.2; 8482 -5.8; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 -1.1; 13660 -4.4; 15026 -2.5; 16529 -0.1; 18182 0.0; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Push GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-6**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Push ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 1.32 | -9.3 dB |
| Peaking | 21 Hz    | 0.18 | -7.0 dB |
| Peaking | 163 Hz   | 0.57 | -7.9 dB |
| Peaking | 6194 Hz  | 1.07 | -7.7 dB |
| Peaking | 21063 Hz | 1.44 | -2.2 dB |
| Peaking | 839 Hz   | 2.51 | 2.2 dB  |
| Peaking | 1739 Hz  | 1.53 | -2.2 dB |
| Peaking | 8002 Hz  | 4.01 | -5.6 dB |
| Peaking | 9859 Hz  | 1.08 | 4.1 dB  |
| Peaking | 13822 Hz | 2.71 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Push/Skullcandy%20Push.png)