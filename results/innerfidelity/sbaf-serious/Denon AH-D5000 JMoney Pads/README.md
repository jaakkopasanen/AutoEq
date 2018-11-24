# Denon AH-D5000 JMoney Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 3.5; 25 2.5; 28 1.3; 31 0.6; 34 0.0; 37 -0.3; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.6; 60 -0.6; 66 -0.6; 72 -0.6; 79 -0.8; 87 -1.1; 96 -1.4; 106 -1.5; 116 -1.4; 128 -1.7; 141 -1.7; 155 -1.9; 170 -1.8; 187 -1.8; 206 -1.7; 227 -1.6; 249 -1.5; 274 -1.4; 302 -1.1; 332 -1.0; 365 -1.0; 402 -0.5; 442 0.2; 486 0.3; 535 0.9; 588 1.1; 647 0.5; 712 -0.5; 783 -2.1; 861 -1.7; 947 0.6; 1042 -0.6; 1146 -1.0; 1261 -1.3; 1387 -1.8; 1526 -2.3; 1678 -3.0; 1846 -3.0; 2031 -3.1; 2234 -3.4; 2457 -3.2; 2703 -1.3; 2973 -2.0; 3270 -3.1; 3597 -3.9; 3957 -4.7; 4353 -5.8; 4788 -5.8; 5267 -6.5; 5793 -4.3; 6373 -2.9; 7010 -5.4; 7711 -6.0; 8482 -4.8; 9330 -1.9; 10263 -0.6; 11289 -3.0; 12418 -5.5; 13660 -5.3; 15026 -2.6; 16529 -1.3; 18182 -1.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 JMoney Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 JMoney Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 3.26 | 5.6 dB  |
| Peaking | 1784 Hz  | 1.81 | -2.3 dB |
| Peaking | 5335 Hz  | 0.85 | -5.5 dB |
| Peaking | 13247 Hz | 2.83 | -5.3 dB |
| Peaking | 21751 Hz | 1.62 | -4.2 dB |
| Peaking | 17 Hz    | 0.13 | -0.5 dB |
| Peaking | 167 Hz   | 0.93 | -1.8 dB |
| Peaking | 6259 Hz  | 5.89 | 4.4 dB  |
| Peaking | 8153 Hz  | 1.42 | -3.4 dB |
| Peaking | 9830 Hz  | 3.63 | 4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000%20JMoney%20Pads/Denon%20AH-D5000%20JMoney%20Pads.png)