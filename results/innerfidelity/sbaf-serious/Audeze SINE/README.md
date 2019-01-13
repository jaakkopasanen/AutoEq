# Audeze SINE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.3; 28 2.6; 31 2.0; 34 1.6; 37 1.3; 41 1.0; 45 0.8; 49 0.5; 54 0.3; 60 0.2; 66 -0.0; 72 -0.3; 79 -0.5; 87 -0.9; 96 -1.3; 106 -1.5; 116 -1.7; 128 -2.0; 141 -2.2; 155 -2.3; 170 -2.3; 187 -2.5; 206 -2.6; 227 -2.4; 249 -2.2; 274 -2.1; 302 -2.1; 332 -2.1; 365 -2.0; 402 -1.8; 442 -1.6; 486 -1.4; 535 -1.0; 588 -0.5; 647 -0.0; 712 0.3; 783 0.4; 861 0.4; 947 0.2; 1042 0.1; 1146 0.3; 1261 -0.4; 1387 -1.2; 1526 -1.6; 1678 -2.3; 1846 -2.4; 2031 -2.3; 2234 -2.2; 2457 -1.0; 2703 -1.6; 2973 -1.4; 3270 -0.8; 3597 -1.1; 3957 0.5; 4353 1.0; 4788 2.0; 5267 3.2; 5793 4.2; 6373 3.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -1.8; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.1; 18182 -3.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze SINE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.85 | 5.8 dB  |
| Peaking | 193 Hz   | 0.67 | -2.7 dB |
| Peaking | 2077 Hz  | 1.59 | -2.5 dB |
| Peaking | 5786 Hz  | 2.85 | 4.6 dB  |
| Peaking | 17979 Hz | 2.12 | -3.5 dB |
| Peaking | 13 Hz    | 0.75 | 0.8 dB  |
| Peaking | 469 Hz   | 1.29 | -2.1 dB |
| Peaking | 651 Hz   | 0.8  | 1.9 dB  |
| Peaking | 1631 Hz  | 3.52 | -0.9 dB |
| Peaking | 10257 Hz | 6.68 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE/Audeze%20SINE.png)