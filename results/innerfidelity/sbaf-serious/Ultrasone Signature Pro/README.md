# Ultrasone Signature Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.2; 28 2.2; 31 1.5; 34 0.9; 37 0.5; 41 0.0; 45 -0.3; 49 -0.6; 54 -0.8; 60 -1.0; 66 -1.0; 72 -0.4; 79 0.3; 87 -0.6; 96 -1.9; 106 -2.1; 116 -1.3; 128 -2.0; 141 -2.9; 155 -3.1; 170 -2.2; 187 -3.0; 206 -3.0; 227 -2.7; 249 -2.5; 274 -1.9; 302 -1.4; 332 -1.1; 365 -0.9; 402 -0.9; 442 -0.9; 486 -1.3; 535 -1.5; 588 -1.4; 647 -1.4; 712 -1.4; 783 -1.1; 861 -1.0; 947 -0.5; 1042 0.4; 1146 1.0; 1261 0.8; 1387 0.3; 1526 0.8; 1678 2.2; 1846 2.9; 2031 3.9; 2234 5.8; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 5.9; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -2.5; 11289 -3.1; 12418 -1.8; 13660 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Signature Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.89 | 5.2 dB  |
| Peaking | 169 Hz   | 1.57 | -1.6 dB |
| Peaking | 489 Hz   | 0.18 | -1.8 dB |
| Peaking | 3720 Hz  | 0.52 | 7.4 dB  |
| Peaking | 10475 Hz | 1.56 | -4.9 dB |
| Peaking | 381 Hz   | 2.28 | 1.3 dB  |
| Peaking | 1413 Hz  | 0.21 | -0.6 dB |
| Peaking | 2341 Hz  | 4.36 | 2.1 dB  |
| Peaking | 6222 Hz  | 4.02 | 2.2 dB  |
| Peaking | 7510 Hz  | 6.81 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Signature%20Pro/Ultrasone%20Signature%20Pro.png)