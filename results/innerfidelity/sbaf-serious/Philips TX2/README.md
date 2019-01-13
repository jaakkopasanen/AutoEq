# Philips TX2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -6.5; 23 -6.5; 25 -6.5; 28 -6.5; 31 -6.5; 34 -6.4; 37 -6.4; 41 -6.4; 45 -6.4; 49 -6.4; 54 -6.4; 60 -6.5; 66 -6.5; 72 -6.6; 79 -6.7; 87 -6.8; 96 -6.9; 106 -6.8; 116 -6.6; 128 -6.6; 141 -6.4; 155 -6.2; 170 -5.9; 187 -5.5; 206 -5.2; 227 -4.6; 249 -4.2; 274 -3.7; 302 -3.2; 332 -2.7; 365 -2.2; 402 -1.8; 442 -1.3; 486 -0.4; 535 -0.4; 588 0.3; 647 0.6; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -1.1; 1387 -1.8; 1526 -2.6; 1678 -3.3; 1846 -3.8; 2031 -4.2; 2234 -4.2; 2457 -3.0; 2703 -1.4; 2973 0.9; 3270 2.8; 3597 3.5; 3957 2.5; 4353 -0.3; 4788 -2.2; 5267 -3.6; 5793 -3.8; 6373 -3.5; 7010 -1.5; 7711 -0.7; 8482 -1.5; 9330 -1.4; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips TX2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 60 Hz   | 0.25 | -7.2 dB |
| Peaking | 2093 Hz | 2.04 | -5.0 dB |
| Peaking | 3548 Hz | 2.73 | 5.4 dB  |
| Peaking | 5554 Hz | 2.28 | -4.6 dB |
| Peaking | 8989 Hz | 6.77 | -1.2 dB |
| Peaking | 18 Hz   | 1.07 | -1.8 dB |
| Peaking | 55 Hz   | 0.88 | 1.2 dB  |
| Peaking | 172 Hz  | 0.63 | -1.0 dB |
| Peaking | 686 Hz  | 1.11 | 1.9 dB  |
| Peaking | 1499 Hz | 3.35 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX2/Philips%20TX2.png)