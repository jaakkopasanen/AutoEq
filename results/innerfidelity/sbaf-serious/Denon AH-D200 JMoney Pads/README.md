# Denon AH-D200 JMoney Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.4; 28 4.6; 31 3.9; 34 3.5; 37 3.3; 41 3.1; 45 3.1; 49 3.0; 54 3.2; 60 3.4; 66 3.3; 72 3.1; 79 2.8; 87 2.5; 96 2.2; 106 2.0; 116 1.9; 128 1.7; 141 1.6; 155 1.5; 170 1.6; 187 1.5; 206 1.6; 227 1.9; 249 1.9; 274 1.9; 302 1.9; 332 1.9; 365 2.1; 402 1.9; 442 1.9; 486 1.2; 535 0.8; 588 0.6; 647 -0.1; 712 -0.6; 783 1.3; 861 -0.2; 947 -0.2; 1042 0.2; 1146 1.0; 1261 1.4; 1387 1.3; 1526 0.9; 1678 0.6; 1846 0.8; 2031 1.2; 2234 1.4; 2457 1.0; 2703 0.9; 2973 2.0; 3270 1.4; 3597 -0.6; 3957 -1.6; 4353 -1.8; 4788 -0.7; 5267 -2.8; 5793 -0.6; 6373 1.1; 7010 -1.9; 7711 -2.2; 8482 -0.8; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D200 JMoney Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D200 JMoney Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.12 | 5.7 dB  |
| Peaking | 66 Hz   | 0.91 | 2.6 dB  |
| Peaking | 308 Hz  | 0.75 | 1.8 dB  |
| Peaking | 5151 Hz | 3.5  | -2.1 dB |
| Peaking | 677 Hz  | 6.52 | -1.5 dB |
| Peaking | 3029 Hz | 0.87 | 1.8 dB  |
| Peaking | 3992 Hz | 4.15 | -2.9 dB |
| Peaking | 6265 Hz | 9.86 | 2.6 dB  |
| Peaking | 7366 Hz | 3.81 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D200%20JMoney%20Pads/Denon%20AH-D200%20JMoney%20Pads.png)