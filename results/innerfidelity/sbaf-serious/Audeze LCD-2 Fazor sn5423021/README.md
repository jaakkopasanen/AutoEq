# Audeze LCD-2 Fazor sn5423021
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.7; 41 5.3; 45 4.9; 49 4.9; 54 4.6; 60 3.7; 66 3.1; 72 2.9; 79 2.9; 87 2.7; 96 2.4; 106 2.1; 116 2.0; 128 1.7; 141 1.5; 155 1.3; 170 1.1; 187 0.9; 206 0.8; 227 0.9; 249 0.8; 274 0.7; 302 0.7; 332 0.6; 365 0.5; 402 0.5; 442 0.6; 486 0.4; 535 0.5; 588 1.0; 647 1.1; 712 1.0; 783 0.8; 861 0.3; 947 0.1; 1042 0.2; 1146 0.1; 1261 0.2; 1387 -0.8; 1526 -1.6; 1678 -1.7; 1846 -0.8; 2031 0.2; 2234 0.8; 2457 1.8; 2703 2.8; 2973 3.8; 3270 4.6; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Fazor sn5423021 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Fazor sn5423021 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.29 | 6.2 dB  |
| Peaking | 655 Hz  | 2.24 | 0.9 dB  |
| Peaking | 1653 Hz | 2.89 | -2.8 dB |
| Peaking | 4387 Hz | 1.16 | 6.9 dB  |
| Peaking | 70 Hz   | 4.52 | -0.6 dB |
| Peaking | 3537 Hz | 3.02 | 1.0 dB  |
| Peaking | 4289 Hz | 3.45 | -1.2 dB |
| Peaking | 6303 Hz | 2.98 | 4.7 dB  |
| Peaking | 7368 Hz | 1.59 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Fazor%20sn5423021/Audeze%20LCD-2%20Fazor%20sn5423021.png)