# Master Dynamic MH40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.1; 28 1.0; 31 0.8; 34 0.7; 37 0.5; 41 0.4; 45 0.4; 49 0.3; 54 0.3; 60 0.3; 66 0.3; 72 0.3; 79 -0.2; 87 -0.9; 96 -1.6; 106 -1.3; 116 -1.3; 128 -1.9; 141 -2.7; 155 -2.3; 170 -1.2; 187 -2.1; 206 -1.5; 227 -0.7; 249 0.2; 274 1.2; 302 2.0; 332 2.7; 365 3.6; 402 4.0; 442 4.3; 486 3.9; 535 3.4; 588 2.8; 647 1.8; 712 1.0; 783 0.7; 861 0.2; 947 0.1; 1042 0.0; 1146 -0.1; 1261 -0.1; 1387 -0.4; 1526 -0.7; 1678 -0.6; 1846 -0.3; 2031 0.5; 2234 2.6; 2457 2.2; 2703 -0.3; 2973 1.6; 3270 3.9; 3597 4.4; 3957 5.5; 4353 5.5; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic MH40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic MH40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.2  | 1.3 dB  |
| Peaking | 153 Hz  | 0.99 | -2.8 dB |
| Peaking | 418 Hz  | 1.48 | 4.9 dB  |
| Peaking | 4140 Hz | 2.09 | 5.3 dB  |
| Peaking | 5837 Hz | 3.41 | 5.0 dB  |
| Peaking | 927 Hz  | 4.11 | -0.4 dB |
| Peaking | 1852 Hz | 1.74 | -2.7 dB |
| Peaking | 2377 Hz | 2    | 4.1 dB  |
| Peaking | 2738 Hz | 6.91 | -4.3 dB |
| Peaking | 8938 Hz | 3.99 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20MH40/Master%20Dynamic%20MH40.png)