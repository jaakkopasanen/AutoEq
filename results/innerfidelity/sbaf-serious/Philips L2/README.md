# Philips L2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -3.9; 23 -4.4; 25 -4.8; 28 -5.2; 31 -5.5; 34 -5.8; 37 -5.9; 41 -6.1; 45 -6.1; 49 -6.1; 54 -6.0; 60 -6.0; 66 -5.8; 72 -5.7; 79 -5.5; 87 -5.3; 96 -5.1; 106 -5.1; 116 -5.1; 128 -5.4; 141 -4.8; 155 -4.5; 170 -3.8; 187 -4.0; 206 -3.8; 227 -3.4; 249 -3.3; 274 -2.9; 302 -2.3; 332 -2.1; 365 -1.7; 402 -1.3; 442 -0.7; 486 -0.4; 535 0.1; 588 0.7; 647 1.1; 712 1.0; 783 0.9; 861 0.4; 947 0.0; 1042 -0.1; 1146 0.3; 1261 -0.9; 1387 -2.9; 1526 -4.8; 1678 -6.0; 1846 -6.7; 2031 -6.8; 2234 -6.4; 2457 -6.2; 2703 -5.3; 2973 -4.1; 3270 -2.4; 3597 -1.1; 3957 0.3; 4353 2.4; 4788 4.1; 5267 5.3; 5793 1.7; 6373 -1.8; 7010 -3.0; 7711 -2.4; 8482 -1.5; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -2.8; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips L2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips L2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.43 | -6.0 dB |
| Peaking | 171 Hz   | 0.98 | -2.6 dB |
| Peaking | 2137 Hz  | 1.6  | -7.5 dB |
| Peaking | 4983 Hz  | 5.03 | 6.7 dB  |
| Peaking | 674 Hz   | 3.12 | 1.7 dB  |
| Peaking | 1328 Hz  | 1.44 | 2.5 dB  |
| Peaking | 1542 Hz  | 3.15 | -3.8 dB |
| Peaking | 7185 Hz  | 4.23 | -3.5 dB |
| Peaking | 19009 Hz | 2.27 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20L2/Philips%20L2.png)