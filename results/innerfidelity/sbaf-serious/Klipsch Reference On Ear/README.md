# Klipsch Reference On Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.5; 28 -4.6; 31 -4.8; 34 -4.8; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.9; 54 -4.8; 60 -4.8; 66 -5.0; 72 -5.2; 79 -5.3; 87 -5.5; 96 -5.7; 106 -5.7; 116 -5.9; 128 -6.2; 141 -6.1; 155 -6.4; 170 -6.1; 187 -6.4; 206 -6.6; 227 -6.4; 249 -6.2; 274 -5.8; 302 -5.4; 332 -5.2; 365 -5.5; 402 -5.0; 442 -4.5; 486 -5.1; 535 -4.8; 588 -4.0; 647 -3.6; 712 -3.1; 783 -2.1; 861 -1.4; 947 -0.5; 1042 0.4; 1146 1.3; 1261 2.0; 1387 1.6; 1526 1.7; 1678 1.7; 1846 1.8; 2031 2.1; 2234 2.7; 2457 2.7; 2703 2.2; 2973 1.5; 3270 0.9; 3597 0.6; 3957 0.6; 4353 1.1; 4788 2.9; 5267 5.9; 5793 4.1; 6373 1.8; 7010 1.1; 7711 -1.6; 8482 -4.0; 9330 -4.1; 10263 -1.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.28 | -3.9 dB |
| Peaking | 221 Hz  | 0.52 | -5.0 dB |
| Peaking | 603 Hz  | 1.01 | -4.1 dB |
| Peaking | 1415 Hz | 0.35 | 3.1 dB  |
| Peaking | 23 Hz   | 1.25 | -0.6 dB |
| Peaking | 2464 Hz | 5.29 | 0.9 dB  |
| Peaking | 4125 Hz | 1.67 | -2.1 dB |
| Peaking | 5335 Hz | 3.75 | 6.3 dB  |
| Peaking | 8844 Hz | 3.8  | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20On%20Ear/Klipsch%20Reference%20On%20Ear.png)